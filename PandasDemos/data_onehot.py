import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.DataFrame({"k1":[1,2,3,4], "k2":[2.4, 3.0,5.1,1.6], "k3":["1", "1_3", "6_3_4_7","7_4_5"], "k4": [(1,), (1, 2, 3), (1,4,6,7,8), (2,5)]},
                  index=['a', 'b', 'c', 'd'])


# 对某个多值的series进行one-hot编码
def one_hot_mapper(series, prefix='pre_'):
    assert prefix
    if isinstance(series[0],tuple):
        series_list = series.copy()
    elif isinstance(series[0],str):
        series_list = series.str.split("_")     # 需要one-hot的特征的格式化
    else:
        raise TypeError
    series_index = series_list.index
    mapper_list = []
    for i in range(series_index.size):
        for value in series_list[i]:
            if value not in mapper_list:
                mapper_list.append(value)
    mapper_list = sorted(mapper_list)
    feature_one_hot_shape = (series_index.size, len(mapper_list))
    feature_one_hot_np = np.zeros(shape=feature_one_hot_shape)
    feature_one_hot_pd = pd.DataFrame(feature_one_hot_np, index=series_index, columns=[prefix + str(i) for i in mapper_list])

    for i in range(series_index.size):
        for value in series_list[i]:
            feature_one_hot_pd.loc[series_index[i], prefix+str(value)] = 1
    return feature_one_hot_pd


if __name__ == '__main__':
    res1 = one_hot_mapper(df['k4'])
    print(res1)
    plt.cm.tab10






