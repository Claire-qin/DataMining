# -*- coding: utf-8 -*-
# @Time : 2019/10/26 上午7:52
# @Author : guofei
# @File : loss_function_plot.py
# @Projcet :
# @Software: PyCharm

"""
绘制常见的损失函数
"""


import numpy as np
import matplotlib.pyplot as plt


# 0-1损失
def zero_one_loss(x):
    x_neg = x[x <= 0]
    x_pos = x[x >= 0]
    y_neg = np.ones_like(x_neg)
    y_pos = np.zeros_like(x_pos)
    return np.concatenate([x_neg, x_pos]), np.concatenate([y_neg, y_pos])


# log损失
def log_loss(x):
    def log_func(s):
        return -np.log2(1/(1+np.exp(-s)))

    y = np.frompyfunc(log_func, 1, 1)(x)
    return y


# 指数损失
def exp_loss(x):
    def exp_func(s):
        return np.exp(-s)

    y = np.frompyfunc(exp_func, 1, 1)(x)
    return y


# hinge损失
def hinge_loss(x):
    def hinge_func(s):
        if 1 - s > 0:
            return 1 - s
        else:
            return 0
    y = np.frompyfunc(hinge_func, 1, 1)(x)
    return y


# MSE损失
def mse_loss(x):
    def mse_func(s):
        return s**2
    y = np.frompyfunc(mse_func, 1, 1)(x)
    return y


# MAE损失
def mae_loss(x):
    def mae_func(s):
        return np.abs(s)
    y = np.frompyfunc(mae_func, 1, 1)(x)
    return y


# log-cosh损失
def log_cosh_loss(x):
    def log_cosh_func(s):
        return np.log2(np.cosh(s))
    y = np.frompyfunc(log_cosh_func, 1, 1)(x)
    return y


# tube损失
def tube_loss(x):
    def tube_func(s, epsilon=0.3):
        return 0 if np.abs(s) <= epsilon else np.abs(s) - epsilon
    y = np.frompyfunc(tube_func, 1, 1)(x)
    return y


# huber损失
def huber_loss(x):
    def huber_func(s, epsilon=0.3):
        return 1/2*s**2 if np.abs(s) <= epsilon else epsilon*np.abs(s) - 1/2*epsilon**2
    y = np.frompyfunc(huber_func, 1, 1)(x)
    return y

# quantile损失
def quantile_loss(x):
    def quantile_func(s, q=0.3):
        return np.max([q*s, (q-1)*s])

    y = np.frompyfunc(quantile_func, 1, 1)(x)
    return y


if __name__ == '__main__':
    x_ = np.arange(-2, 2, 0.01)
    x1, y1 = zero_one_loss(x_)

    y0 = exp_loss(x_)
    y2 = log_loss(x_)
    y3 = hinge_loss(x_)
    y4 = mse_loss(x_)
    y5 = log_cosh_loss(x_)
    y6 = mae_loss(x_)
    y7 = tube_loss(x_)
    y8 = huber_loss(x_)
    y9 = quantile_loss(x_)

    fig = plt.figure()
    plt.plot(x1, y1, label='0-1损失')
    plt.plot(x_, y2, label='Log损失')
    plt.plot(x_, y3, label='Hinge损失')
    plt.plot(x_, y0, label='指数损失')



    # plt.plot(x_, y4, label='MSE损失')
    # plt.plot(x_, y5, label='Log—Cosh损失')
    # plt.plot(x_, y6, label='MAE损失')
    # plt.plot(x_, y7, label='Tube损失(0.3)')
    # plt.plot(x_, y8, label="Huber损失(0.3)")
    # plt.plot(x_, y9, label="Quantile损失(0.3)")

    plt.legend()
    plt.show()

