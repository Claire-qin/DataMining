# -*- coding: utf-8 -*-
# @Time : 2020/1/7 下午12:49
# @Author : guofei
# @File : logging_Filter_sample.py
# @Projcet : 展示过滤器Filter的使用
# @Software: PyCharm

import logging
import sys

class ContextFilter(logging.Filter):
    """
    这是一个控制日志记录的过滤器。
    """
    def filter(self, record):
        try:
            filter_key = record.TASK
        except AttributeError:
            return False

        if filter_key == "logToConsole":   # 仅记录Task=logToConsole的消息
            return True
        else:
            return False

logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.WARN)

console_fmt = '%(asctime)-15s [%(TASK)s] %(message)s'
console_formatter = logging.Formatter(console_fmt)
console_handler.setFormatter(console_formatter)

console_filter = ContextFilter()
console_handler.addFilter(console_filter)
logger.addHandler(console_handler)

filter_dict = {'TASK': 'logToConsole'}

# 记录日志
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message1', extra=filter_dict)
logger.error('error message2')