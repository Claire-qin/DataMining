# -*- coding: utf-8 -*-
# @Time : 2020/1/7 上午10:38
# @Author : guofei
# @File : logging_fileconfig_sample.py
# @Projcet :  使用配置文件fileConfig进行日志文件的配置
# @Software: PyCharm

import logging.config

# 读取日志配置文件内容
logging.config.fileConfig('logging.conf')

# 创建一个日志器logger
logger = logging.getLogger('simpleExample')

# 日志输出
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

