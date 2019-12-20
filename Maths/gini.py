# -*- coding: utf-8 -*-
# @Time : 2019/11/23 下午7:04
# @Author : guofei
# @File : gini.py
# @Projcet :
# @Software: PyCharm

"""
对比熵和Gini系数
"""

from sklearn.tree import DecisionTreeClassifier


import matplotlib.pyplot as plt
import numpy as np


p = np.arange(0, 1.01, 0.01)
entropy = [0 if i in [0, 1] else (-i*np.log2(i)-(1-i)*np.log2(1-i))/2 for i in p]
gini = 1 - p ** 2 - (1-p)**2


plt.plot(p, entropy, label='entropy/2')
plt.plot(p, gini, label='gini')
plt.legend()
plt.show()


