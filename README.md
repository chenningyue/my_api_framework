# cny_my_api_framework — 接口自动化测试框架（练手版）

基于 **Python + pytest + requests** 的分层接口自动化框架。练手对象是两个公开接口：

- Swagger **Petstore**（`https://petstore.swagger.io/v2`）—— GET/POST/PUT/DELETE 都有，练增删改查
- **httpbin**（`https://httpbin.org`）—— 练带 token 鉴权（`/bearer` 无 token 返回 401，有 token 返回 200）

> 这个仓库是「从 0 搭一套接口自动化框架」的学习产出物，目标是：**别人 clone 下来，装依赖，就能跑**。

## 目录结构

```
my_api_framework/
├── config/            # 配置层：统一管理 base_url
│   └── config.py
├── common/            # 公共层：发请求、日志、读数据
│   ├── base_request.py   # 封装 requests，统一 get/post/put/patch/delete
│   ├── logger.py         # 专属日志器，落盘 log.txt
│   └── read_data.py      # 从 json 读测试数据
├── data/              # 数据层：测试数据（数据驱动）
│   └── test_data.json
├── api/               # 接口层：每个接口封装成一个类/方法
│   ├── pet_api.py
│   └── bearer_api.py
├── testcase/          # 用例层：只写用例和断言
│   ├── test_pet.py
│   └── test_bearer.py
├── conftest.py        # 让 pytest 把框架根目录加进路径（解决 from api/common/config 的导入）
├── pytest.ini         # pytest 配置（-v 输出、markers 标记）
├── requirements.txt   # 依赖清单
└── README.md          # 本文件
```

## 环境准备

- Python 3.11+
- 装依赖：`pip install -r requirements.txt`

## 怎么跑

```bash
cd my_api_framework
pytest -v              # 跑全部用例
pytest -m smoke        # 只跑冒烟用例
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
