# -*- coding: utf-8 -*-
# @Time : 2019/12/1 上午10:51
# @Author : guofei
# @File : plot_learning_curve.py
# @Projcet :
# @Software: PyCharm


def plot_learning_curve(estimator, title, X, y,
                        ax=None,  # 选择子图
                        ylim=None,  # 设置纵坐标的取值范围
                        cv=None,  # 交叉验证
                        n_jobs=None  # 设定索要使用的线程
                        ):
    from sklearn.model_selection import learning_curve
    import matplotlib.pyplot as plt
    import numpy as np

    train_sizes, train_scores, test_scores = learning_curve(estimator, X, y, shuffle=True, cv=cv, random_state=420, n_jobs=n_jobs)
    # cv可以是数字，也可以是KFold(n_splits=5, shuffle = True, random_state=42)等对象

    if ax == None:
        ax = plt.gca()
    else:
        ax = plt.figure()
    ax.set_title(title)
    if ylim is not None:
        ax.set_ylim(*ylim)
    ax.set_xlabel("Training examples")
    ax.set_ylabel("Score")
    ax.grid()  # 绘制网格，不是必须
    ax.plot(train_sizes, np.mean(train_scores, axis=1), 'o-'
            , color="r", label="Training score")
    ax.plot(train_sizes, np.mean(test_scores, axis=1), 'o-'
            , color="g", label="Test score")
    ax.legend(loc="best")
    return ax

