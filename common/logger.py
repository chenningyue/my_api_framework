import logging

logger = logging.getLogger("api")  # 专属命名 logger，不再依赖 root
logger.setLevel(logging.INFO)  # 级别直接设在自己身上

fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

if not logger.handlers:  # 防止重复添加（被 import 多次也只加一次）
    fh = logging.FileHandler("log.txt", encoding="utf-8")
    fh.setFormatter(fmt)
    logger.addHandler(fh)  # 文件 handler 挂在「我」身上，不挂 root

    sh = logging.StreamHandler()
    sh.setFormatter(fmt)
    logger.addHandler(sh)  # 屏幕 handler 也挂「我」身上

logger.propagate = False
