# -*- coding: utf-8 -*-
# @Time : 2019/12/1 上午11:32
# @Author : guofei
# @File : learning_curve_plus_variance.py
# @Projcet :
# @Software: PyCharm

"""
在常规的validation curve中只通过偏差值来进行判断，实际中往往要记入方差的影响
"""
from xgboost import XGBRegressor as XGBR
from sklearn.model_selection import cross_val_score as CVS
import numpy as np
import matplotlib.pyplot as plt

axisx = range(100,300,10)
rs = []
var = []
ge = []
for i in axisx:
    reg = XGBR(n_estimators=i,random_state=420)
    cvresult = CVS(reg,Xtrain,Ytrain,cv=cv)
    rs.append(cvresult.mean())
    var.append(cvresult.var())
    ge.append((1 - cvresult.mean())**2+cvresult.var())

print(axisx[rs.index(max(rs))],max(rs),var[rs.index(max(rs))])
print(axisx[var.index(min(var))],rs[var.index(min(var))],min(var))
print(axisx[ge.index(min(ge))],rs[ge.index(min(ge))],var[ge.index(min(ge))],min(ge))
rs = np.array(rs)
var = np.array(var)*0.01
plt.figure(figsize=(20,5))
plt.plot(axisx,rs,c="black",label="XGB")
#添加方差线
plt.plot(axisx,rs+var,c="red",linestyle='-.')
plt.plot(axisx,rs-var,c="red",linestyle='-.')
plt.legend()
plt.show()
