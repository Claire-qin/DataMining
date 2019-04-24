"""
处理时间的模块
时间的格式主要有三种：时间戳、结构化时间、格式化时间字符串
"""

# # 模块一：Time模块
# import time
# # 生成时间戳格式
# print(time.time())
#
# # 格式化时间字符串
# print(time.ctime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))   # 缺省值按照本地时间换算
#
# # 结构化时间
# print(time.gmtime())
# print(time.localtime())
#
#
# # 时间戳转结构化时间
# print(time.gmtime(time.time()))
# print(time.localtime((time.time())))
#
#
# # 时间戳转格式化时间字符串
# print(time.ctime(time.time()))
#
#
# # 结构化时间转时间戳
# print(time.mktime(time.localtime()))
#
#
# # 结构化时间转格式化的时间字符串
# print(time.asctime(time.localtime()))
# print(time.strftime('%Y-%m-%d', time.localtime()))
#
#
# # 格式化的时间字符串转结构化时间
# time.strptime(time.strftime("%Y-%m-%d %H:%M:%S"), '%Y-%m-%d %H:%M:%S')
# time.strptime(time.ctime(), '%a %b %d %H:%M:%S %Y')
#
# # 格式化时间转时间戳
# time.mktime(time.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y"))
# time.mktime(time.strptime(time.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S"))


# 模块二：Calendar模块
import calendar



# 模块三：Datetime模块
# import datetime
# datetime.timedelta()


# 模块四：pandas中的时间处理
import numpy as np
import pandas as pd
# np.timedelta64(1*60*60*24*30, 's')

t = pd.DataFrame({"time": ["2018-12-18 00:00:00", "2018-12-19 00:00:00", "2018-12-20 00:00:00", "2018-12-21 00:00:00", "2018-12-22 00:00:00", "2018-12-23 00:00:00"]})
t['time1'] = pd.to_datetime(t['time'])
t['time2'] = t['time1'].shift()