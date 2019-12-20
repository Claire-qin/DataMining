# -*- coding: utf-8 -*-
# @Time : 2019/11/25 上午10:15
# @Author : guofei
# @File : DTC.py
# @Projcet :
# @Software: PyCharm

"""
分类树 Decision Tree Classifer
"""

from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor, ExtraTreeClassifier, ExtraTreeRegressor
from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor, AdaBoostClassifier, AdaBoostRegressor
from sklearn.utils import compute_sample_weight
from xgboost import XGBClassifier, XGBRegressor
import xgboost

xgboost.DMatrix()
xgboost.train()
xgb = XGBClassifier()
xgb.fit(xgb_model=)



clf = RandomForestClassifier()
clf.fit()
