# cny_my_api_framework — 接口自动化测试框架

基于 **Python + pytest + requests + pymysql** 的分层自动化测试框架，包含两块：

- **接口自动化**：对象是两个公开接口——Swagger **Petstore**（增删改查）、**httpbin**（带 token 鉴权）
- **数据库校验**：测试工程师的日常「**调接口 → 查库 → 断言一致**」

> 这个仓库是「从 0 搭一套自动化框架」的产出物，目标是：**别人 clone 下来，装依赖，就能跑；push 到 GitHub 后 CI 自动跑**。

## 目录结构

```
my_api_framework/
├── config/            # 配置层：base_url、数据库连接
│   ├── config.py                 # 接口 base_url
│   ├── db_config.ini             # 数据库配置（含密码，本地文件，已 gitignore）
│   └── db_config.example.ini     # 数据库配置模板（可提交，复制后填密码）
├── common/            # 公共层：发请求、日志、读数据、查库
│   ├── base_request.py   # 封装 requests，统一 get/post/put/patch/delete
│   ├── logger.py         # 专属日志器，落盘 log.txt
│   ├── read_data.py      # 从 json 读测试数据
│   └── db.py             # pymysql 连库、执行 SQL（返回 list[dict]）
├── data/              # 数据层：测试数据（数据驱动）
│   └── test_data.json
├── api/               # 接口层：每个接口封装成一个类/方法
│   ├── pet_api.py
│   └── bearer_api.py
├── testcase/          # 用例层：只写用例和断言
│   ├── test_pet.py
│   ├── test_bearer.py
│   └── test_db_api_consistency.py   # 调接口→查库校验（标了 @pytest.mark.db）
├── mock_app.py        # Flask mock 接口（本地假后端，背后查 school 库）
├── conftest.py        # 把框架根目录加进 sys.path
├── pytest.ini         # pytest 配置（-v、markers：smoke / db）
├── requirements.txt   # 依赖清单
├── .github/workflows/ # CI 配置（push 自动跑，跳过 db 用例）
│   └── ci.yml
└── README.md          # 本文件
```

## 环境准备

- Python 3.11+
- 装依赖：`pip install -r requirements.txt`

**数据库（跑 db 用例才需要）**：

1. 本地装好 MySQL，执行下面的建库建表 SQL（见「数据库校验」一节）；
2. 复制 `config/db_config.example.ini` 为 `config/db_config.ini`，把 `password` 改成你自己的；
3. `config/db_config.ini` 已被 gitignore，**密码不会进 git**。

## 怎么跑

```bash
cd my_api_framework
pytest -v              # 跑全部用例（含 db）
pytest -m smoke        # 只跑冒烟用例
pytest -m "not db"     # 跳过数据库用例（CI 上这么跑，因为 CI 没有 MySQL）
```

## 报告

```bash
# pytest-html（单文件，双击可开）
pytest --html=report.html --self-contained-html

# allure
pytest --alluredir=allure-results
allure serve allure-results
```

## 分层思路（一句话）

**config 管配置、common 管公共能力、api 管接口、data 管数据、testcase 只管断言**——改接口、改数据、改断言互不影响。

### 数据驱动示例

`data/test_data.json` 里 `bearer_cases` 写了两条用例：

```json
{"name": "无token", "token": null, "expect": 401},
{"name": "有token", "token": "mytoken123", "expect": 200}
```

改这里的 `expect`（比如 200 → 999），`test_bearer` 会自动失败——**改数据不改代码**。

## 数据库校验（调接口 → 查库）

这是测试工程师的日常：**测一个接口，光看它返回 200 不够，还要查数据库确认数据真的落库/一致**。

本仓库用 Flask 搭了个本地 mock 接口 `mock_app.py`（`GET /students` 背后查 `school` 库），`test_db_api_consistency.py` 里做三件事：

1. **调接口**：`app.test_client().get("/students")` 拿接口返回；
2. **查库**：`query("SELECT ... FROM students")` 直接查数据库；
3. **校验**：断言两者一致（`assert api_data == db_data`）。

建库建表 SQL（跑 db 用例前先执行）：

```sql
CREATE DATABASE IF NOT EXISTS school DEFAULT CHARSET utf8mb4;
USE school;
CREATE TABLE students (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(20),
  class_name VARCHAR(20)
);
INSERT INTO students (name, class_name) VALUES
('张三','一班'), ('李四','一班'), ('王五','二班'), ('赵六','二班'), ('张三','二班');
```

## CI（GitHub Actions）

push 到 `main` 自动触发：**拉代码 → 装依赖 → 跑测试（`pytest -m "not db"`）→ 出报告**。

> 为什么 CI 跳过 db 用例：CI 的 Linux 上没有你的 MySQL、也连不到你本机的 localhost 数据库，所以标了 `@pytest.mark.db` 的用例在 CI 上跳过、只在本地跑。
