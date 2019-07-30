"""
对pandas的某些列进行分组填充缺失值
dataframe在通过series类型进行填充时，可以通过设置其index值与df的columns值一致来保证填充的正确性
series在通过series类型进行填充时，可以通过保证index一致的方式来保证两者的相同性
"""

import pandas as pd
import numpy as np


def fast_fillna(data):
    # 快速了解用series进行填充的规则
    # fill_series1 = pd.Series({'value': 6, 'value2': 10})   # 类似于用dict进行填充
    # data2 = data.fillna(fill_series1)
    # print(data2)

    fill_series2 = pd.Series({'B': 20, 'D': 100})
    data['value2'].fillna(fill_series2, inplace=True)
    print(data)


def split_fillna(data, columns, by, method='mean'):
    # 方法一：对原df进行先拆分填缺省值，再组合的操作
    # 需要先进行reset_index(）等操作
    # 暂时提供了mean、max和min三种方法
    assert isinstance(data, pd.DataFrame)
    assert isinstance(columns, list)
    index = data.index
    byvalues = data[by].unique()
    filled_data = pd.DataFrame()
    for byvalue in byvalues:
        data_index = data[by]==byvalue   # 根据每个by列的值选取指定的行
        if method == 'mean':
            data_filled = data[data_index].fillna(data[data_index][columns].mean())
        elif method == 'max':
            data_filled = data[data_index].fillna(data[data_index][columns].max())
        elif method == 'min':
            data_filled = data[data_index].fillna(data[data_index][columns].min())
        filled_data = filled_data.append(data_filled)   # 进行拼接
    new_df = filled_data.reindex(index)    # 按照原index排列
    return new_df


def groupby_fillna(data, columns, by,  method='mean'):
    # 方法二：的一致性
    # 需要先进行reset_index(）等操作
    assert isinstance(data, pd.DataFrame)
    assert isinstance(columns, list)
    df_filled = None
    if method == 'mean':
        df_filled = data.groupby(by=by)[columns].mean()
    elif method == 'max':
        df_filled = data.groupby(by=by)[columns].max()
    elif method == 'min':
        df_filled = data.groupby(by=by)[columns].min()
    df_nulls = data[columns].isnull()

    # 依次填充每列的缺失值
    for col in columns:
        null_index = df_nulls[col]    # 每列缺失值位置
        by_values = list(data.loc[null_index, by])   # 缺失位置出对应的by列的值
        fill_value = df_filled.loc[by_values, col]

        fill_value.index = data.loc[null_index, col].index   # 将填充值的index改为缺失值所在的index
        data.loc[null_index, col] = fill_value

    return data



if __name__ == '__main__':

    df = pd.DataFrame({'code': [1, 2, 3, 4, 5, 6, 7, 8],
                       'value': [np.nan, 5, 7, 8, 9, 10, 11, 12],
                       'value2': [5, np.nan, 7, np.nan, 9, 10, 11, 12],
                       'industry': ['农业1', '农业1', '农业1', '农业2', '农业2', '农业4', '农业2', '农业3']},
                      index=list('ABCDEFGH'))

    # fast_fillna(df)
    print(df)


    # df2 = split_fillna(df, ['value2'], by='industry')
    # print(df2)

    df3 = groupby_fillna(df, ['value', 'value2'], by='industry', method='min')
    print(df3)








