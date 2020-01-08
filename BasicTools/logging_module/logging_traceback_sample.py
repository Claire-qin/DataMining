# -*- coding: utf-8 -*-
# @Time : 2020/1/8 上午9:46
# @Author : guofei
# @File : logging_traceback_sample.py
# @Projcet : 利用logging进行程序异常的记录
# @Software: PyCharm


import logging


def logger_traceback():
    logger = logging.getLogger('traceback')
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler("trace_log.txt", encoding='utf-8')
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    logger.addHandler(handler)
    logger.addHandler(console)

    logger.info("开始记录日志信息！")
    logger.debug("调试程序！")
    logger.warning("出现某些异常！")
    try:
        open("destination.txt", "rb")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        logger.error("无法打开destination.txt", exc_info=True)

    logger.info("日记记录结束！")


if __name__ == '__main__':
    logger_traceback()

