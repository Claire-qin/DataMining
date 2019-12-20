# -*- coding: utf-8 -*-
# @Time : 2019/12/6 下午4:25
# @Author : guofei
# @File : 1.py
# @Projcet :
# @Software: PyCharm

from sklearn.model_selection import ShuffleSplit,
from sklearn.metrics import make_scorer
from sklearn.compose import ColumnTransformer
import numpy as np

X = np.array([[1, 2], [3, 4], [1, 2], [3, 4], [5, 6], [6, 5], [7, 8], [8, 7]])
kfold = ShuffleSplit(n_splits=5, test_size=0.3)

for train, test in kfold.split(X):
    print(train)
    print(test)
    print("------")