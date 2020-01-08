# -*- coding: utf-8 -*-
# @Time : 2020/1/6 下午4:31
# @Author : guofei
# @File : logging_directAPI_sample.py
# @Projcet : 通过模块级的函数进行日志文件的输出
# @Software: PyCharm

import logging


def terminal_logging():
    # 终端输出日志文件
    logging.basicConfig(level='INFO')
    logging.debug("调试日志！")
    logging.info("信息日志！")
    logging.error("错误日志！")


def file_logging():
    # 文件输出日志文件，使用filename则只能写入英文日志，而不能写入中文日志（编码问题）
    logging.basicConfig(level='INFO', filename='logging_directAPI_sample_logging1.log',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filemode='a')
    logging.debug("Debug log")
    logging.info("Info log")
    logging.error("Error log")


def file_chinese_logging():
    # 文件输出日志文件，通过设置stream参数的文件流写入中文日志
    f = open('logging_directAPI_sample_logging2.log', mode='a', encoding='utf-8')
    logging.basicConfig(level='INFO', stream=f)
    logging.debug("调试日志！")
    logging.info("信息日志！")
    logging.error("错误日志！")
    f.close()    # 需手动关闭


if __name__ == '__main__':
    terminal_logging()
    # file_logging()
    # file_chinese_logging()
