"""
需求：对于某个df，每一行的若干列的和为固定值，但每一行总有某一个数(不固定)是缺失的，要求利用已有的值对剩下的值进行填空
"""

import pandas as pd
import numpy as np
import math


def fillna_method1(data:pd.DataFrame(), columns, sum_value):
    """
    采用逐行循环的方式
    :param data: 需要处理的df
    :param columns: 和为固定值的某些列
    :param sum_value: 这些列的和
    :return: fillna之后的data
    """
    for i in data.index:
        columns_tmp = columns.copy()   # 注意深拷贝
        assert data.loc[i, columns].isnull().sum() == 1    # 每行有仅有一个缺失值
        flag = None
        for c in columns_tmp:
            if data.loc[i, c]==np.nan or math.isnan(data.loc[i, c]):
                columns_tmp.remove(c)
                flag = c
                break
        data.loc[i, flag] = sum_value - data.loc[i, columns_tmp].sum()
    return data


def fillna_method2(data:pd.DataFrame(), columns, sum_value):
    # 利用对每行数据进行masked快速计算
    for i, j, k in zip(data.index, data[columns].isnull().values, data[columns].notnull().values):
        assert j.sum() == 1
        columns_changed = pd.Index(columns)[j]
        data.loc[i, columns_changed] = sum_value - data.loc[i, k].sum()
    return data


if __name__ == '__main__':
    df = pd.DataFrame({'A': [np.nan, 1, 5, 6], 'B': [4, 3, np.nan, np.nan], 'C': [66, np.nan, 34, 45], 'D': [1,2,3,4]})
    print(df)
    ddf = fillna_method1(df, ['A','B','C'], 0)
    print(ddf)
