"""
对pandas的某些列进行分组填充缺失值
"""

import pandas as pd
import numpy as np


def split_fillna(data, columns, by):
    # 方法一：对原df进行先拆分填缺省值，再组合的操作
    # 需要先进行reset_index(）等操作
    assert isinstance(data, pd.DataFrame)
    assert isinstance(columns, list)
    index = data.index
    byvalues = data[by].unique()
    filled_data = pd.DataFrame()
    for byvalue in byvalues:
        data_index = data[by]==byvalue   # 根据每个by列的值选取指定的行
        data_filled = data[data_index].fillna(data[data_index][columns].mean())
        filled_data = filled_data.append(data_filled)   # 进行拼接
    new_df = filled_data.reindex(index)    # 按照原index排列
    return new_df


def groupby_fillna(data, columns, by):
    # 方法二：的一致性
    # 需要先进行reset_index(）等操作
    assert isinstance(data, pd.DataFrame)
    assert isinstance(columns, list)
    df_means = data.groupby(by=by)[columns].mean()
    df_nulls = data[columns].isnull()

    # 依次填充每列的缺失值
    for col in columns:
        null_index = df_nulls[col]    # 每列缺失值位置
        by_values = list(data.loc[null_index, by])   # 缺失位置出对应的by列的值
        fill_value = df_means.loc[by_values, col]
        # fill_value.index = df.loc
        fill_value.index = data.loc[null_index, col].index
        data.loc[null_index, col] = fill_value

    return data



if __name__ == '__main__':

    df = pd.DataFrame({'code': [1, 2, 3, 4, 5, 6, 7, 8],
                       'value': [np.nan, 5, 7, 8, 9, 10, 11, 12],
                       'value2': [5, np.nan, 7, np.nan, 9, 10, 11, 12],
                       'industry': ['农业1', '农业1', '农业1', '农业2', '农业2', '农业4', '农业2', '农业3']},
                      index=list('ABCDEFGH'))

    # df2 = split_fillna(df, ['value2'], by='industry')
    # print(df2)

    df3 = groupby_fillna(df, ['value', 'value2'], by='industry')
    print(df3)








