# -*- coding: utf-8 -*-
# @Time : 2019/12/18 下午4:44
# @Author : guofei
# @File : test2.py
# @Projcet :
# @Software: PyCharm


from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectFromModel
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.metrics import mutual_info_score, adjusted_mutual_info_score, normalized_mutual_info_score
from sklearn.metrics import homogeneity_score, completeness_score, homogeneity_completeness_v_measure, v_measure_score
from sklearn.metrics import adjusted_rand_score
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit, train_test_split
import pandas as pd
import numpy as np

index = np.arange(100, 200)    # DataFrame的index
np.random.seed(0)
np.random.shuffle(index)     # 随机打乱
cla = np.random.choice([0, 1], p=[0.2, 0.8], size=100)    # 类别数据

df = pd.DataFrame({"a": np.arange(100), "b": cla}, index=index)

sss = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=64)


# 划分训练集和测试集
for train_index, test_index in sss.split(df, df['b']):
    train_data = df.iloc[train_index]
    test_data = df.iloc[test_index]

    # 将训练集进一步划分为训练数据和验证数据
    for train_index_, validation_index_ in sss.split(train_data['b'], train_data['b']):
        train_data_ = train_data.iloc[train_index_]    # 此时必须为train_data
        validate_data_ = train_data.iloc[validation_index_]   # 此时必须为train_data

        train_index_set = set(train_data_.index)
        validate_index_set = set(validate_data_.index)
        test_index_set = set(test_data.index)

        if train_index_set.intersection(validate_index_set) or train_index_set.intersection(test_index_set) or validate_index_set.intersection(test_index_set):
            print("发生数据交叉")
        else:
            print("数据被隔离划分")



A = pd.DataFrame({"A":[1,2,3], "B":[4,5,6]})
A.groupby()










