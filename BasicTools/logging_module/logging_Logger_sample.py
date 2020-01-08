# -*- coding: utf-8 -*-
# @Time : 2020/1/7 上午9:31
# @Author : guofei
# @File : logging_Logger_sample.py
# @Projcet : 通过Logger进行日志配置
# @Software: PyCharm

import logging


def my_logger():
    """
    共配置了两个Logger对象，父Logger A和子Logger A.B
    父Logger A配置了一个StreamHandler，用于将日志输出文件
    子Logger A.B配置了两个FileHandler，用于分别对日志的level进行控制
    :return:
    """

    logger_parent = logging.getLogger(name='A')    # 父logger
    logger_child = logging.getLogger(name='A.B')    # 子logger
    # logger_child.propagate = 0     # 防止反传消息

    logger_parent.setLevel('DEBUG')     # 必须先设置logger级的level，再设置handler级的，否则会出现错误

    stream_handler = logging.StreamHandler()    # 流文件处理器，此处用于控制写入A.B logger
    stream_handler.setLevel(logging.WARNING)   # handler的level设置
    stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))   # handler的format设置

    file_handler1 = logging.FileHandler('logging_Logger_sample_logger1.log', encoding='utf-8', mode='a+')
    file_handler1.setLevel(logging.INFO)
    file_handler1.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    file_handler2 = logging.FileHandler('logging_Logger_sample_logger2.log', encoding='utf-8', mode='a+')
    file_handler2.setLevel(logging.WARNING)
    file_handler2.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    logger_parent.addHandler(stream_handler)
    logger_child.addHandler(file_handler1)
    logger_child.addHandler(file_handler2)

    logger_parent.warning("parent_logger警告!")
    logger_parent.info('parent_logger消息！')
    logger_parent.debug('parent_logger调试！')

    logger_child.warning("child_logger警告!")
    logger_child.info('child_logger消息！')
    logger_child.debug('child_logger调试！')
    logger_child.error('child_logger错误！')


if __name__ == '__main__':
    my_logger()
