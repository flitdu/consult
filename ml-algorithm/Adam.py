# -*- coding: utf-8 -*-
"""
==============================================================================
Time : 2021/7/10 3:25 下午
Author : Dufy
Email : 813540660@qq.com
File : test.py

关于Adam 优化方法的demo
参考：https://github.com/keras-team/keras/blob/a5a6a53ece/keras/optimizer_v2/adam_test.py
==============================================================================
"""

import traceback
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


class Draw(object):
    def __init__(self):
        self.fig = plt.figure(1, figsize=(12, 8))

    def draw_hill(self, x, y, optimizer):
        """得到三维曲面点"""
        a = np.linspace(-20, 20, 100)
        b = np.linspace(-20, 20, 100)
        x = np.array(x)
        y = np.array(y)

        allSSE = np.zeros(shape=(len(a), len(b)))
        for ai in range(0, len(a)):
            for bi in range(0, len(b)):
                a0 = a[ai]
                b0 = b[bi]
                SSE = optimizer.calc_loss(a0,b0,x,y)
                allSSE[ai][bi] = SSE
        a, b = np.meshgrid(a, b)
        return [a, b, allSSE]

    def draw_scatter_3d(self, a, b, loss):
        # 绘制三维中的loss点
        ax.scatter(a, b, loss, color='black')

    def draw_contour(self, a, b):
        # 绘制等高线
        plt.subplot(2, 2, 2)
        plt.scatter(a,b, s=5, color='blue')

    def draw_regression_curve(self, optimizer, x, y):
        pass
        # 绘制图3中的回归直线
        plt.subplot(2, 2, 3)
        plt.plot(x, y)
        plt.plot(x, y, 'o')
        x_ = np.linspace(-1, 2, 2)
        y_draw = optimizer.a * x_ + optimizer.b
        plt.plot(x_, y_draw)

    def draw_loss_curve(self, all_loss, all_step):
        # 绘制图4的loss更新曲线
        plt.subplot(2, 2, 4)
        plt.plot(all_step, all_loss, color='orange')
        plt.xlabel("step")
        plt.ylabel("loss")


class Optimizer(object):
    def __init__(self):
        self.a = 10
        self.b = -20
        self.lr=0.2
        self.gamma= 0.1  # moment方法上一时刻的系数
        self.ma = 0 # 前一次步伐信息记录
        self.va = 0 # 前一次步伐信息记录
        self.mb = 0 # 前一次步伐信息记录
        self.vb = 0 # 前一次步伐信息记录
        self.beta1 = 0.9
        self.beta2 = 0.999
        self.epsilon = 1e-8

    def iterate(self, x, y, step, random_index=None):
        """参数迭代更新

        :param x:
        :param y: 真实值
        :param step: 迭代步数
        :param random_index: 是否随机梯度下降，当取值不为None,随机梯度下降
        :return: loss：当前损失
        """
        loss = self.calc_loss(self.a, self.b, x, y)
        print((self.a, self.b, loss), '...')  # 显示同一时刻的参数以及对应的loss

        if random_index is None:
            y_ = self.a * x + self.b  # 预测值
            g_ta = sum((y_-y)*x)/len(x)
            g_tb = sum(y_-y)/len(x)
        else:  # SGD
            y_ = self.a * x[random_index] + self.b  # 预测值
            g_ta = (y_-y[random_index])*x[random_index]
            g_tb = y_-y[random_index]

        tmp, self.ma, self.va = self.update_delta_para(self.ma, self.va, g_ta, step)
        self.a -= tmp
        tmp, self.mb, self.vb = self.update_delta_para(self.mb, self.vb, g_tb, step)
        self.b -= tmp
        return loss

    def calc_loss(self, a, b, x, y):
        """计算损失，优化函数

        Loss = (y_-y)^2/(2n)

        :param a:
        :param b:
        :param x:
        :param y: 真实值
        :return:
        """
        y_ = a * x + b
        tmp = (y_ - y) ** 2
        loss = sum(tmp) / (2 * len(x))
        return loss

    def update_delta_para(self, m, v, g_t, t):
        """更新损失函数中的参数改变量

        一方面，Adam记录梯度的一阶矩，即过往梯度与当前梯度的平均，体现了惯性保持；
        另一方面，还记录梯度的二阶矩，即过往梯度平方与当前梯度平方的平均，体现了环境感知能力，
                为不同参数产生自适应的学习速率

        :param m: 上一时刻 一阶矩
        :param v: 上一时刻 二阶矩
        :param g_t: 梯度方向
        :param t: 迭代步数
        :return:
        """
        t += 1
        m = self.beta1*m + (1-self.beta1)*g_t
        v = self.beta2*v + (1-self.beta2)*g_t**2

        mhat_t = m/(1-self.beta1**t)
        vhat_t = v/(1-self.beta2**t)
        delta_param = self.lr * mhat_t / (np.sqrt(vhat_t + self.epsilon))
        return delta_param, m, v


if __name__ == "__main__":
    pass
    x = np.array([30, 35, 37, 59, 70, 76, 88, 100]).astype(np.float32)
    y = np.array([1100, 1423, 1377, 1800, 2304, 2588, 3495, 4839]).astype(np.float32)
    x_max = max(x)
    x_min = min(x)
    y_max = max(y)
    y_min = min(y)
    for i in range(0, len(x)):  # 0-1归一化
        x[i] = (x[i] - x_min) / (x_max - x_min)
        y[i] = (y[i] - y_min) / (y_max - y_min)
    print(x, y, sep='\n')
    # plt.plot(x,y,'-o')
    # plt.show()

    optimizer = Optimizer()
    draw = Draw()
    [ha, hb, hallSSE] = draw.draw_hill(x, y, optimizer)
    hallSSE = hallSSE.T  # 重要，将所有的losses做一个转置。原因是矩阵是以左上角至右下角顺序排列元素，而绘图是以左下角为原点。
    fig = draw.fig
    # 绘制图1的曲面
    ax = fig.add_subplot(2, 2, 1, projection='3d')
    ax.set_top_view()
    ax.plot_surface(ha, hb, hallSSE, rstride=2, cstride=2, cmap='rainbow')
    # 绘制图2的等高线图
    plt.subplot(2, 2, 2)
    ta = np.linspace(-20, 20, 100)
    tb = np.linspace(-20, 20, 100)
    plt.contourf(ha, hb, hallSSE, 15, alpha=0.5, cmap=plt.cm.hot)
    C = plt.contour(ha, hb, hallSSE, 15, colors='black')
    plt.clabel(C, inline=True)
    plt.xlabel('a')
    plt.ylabel('b')

    all_loss = []
    all_step = []
    for step in range(50):
        random_index = random.randint(0, len(x)-1)  # 随机取一个样本点
        pre_a = optimizer.a  # 记录上一时刻的a
        pre_b = optimizer.b

        # loss = optimizer.iterate(x, y, step, random_index)  # SGD，随机梯度下降
        loss = optimizer.iterate(x, y, step)  # 批量梯度下降
        all_loss.append(loss)
        all_step.append(step)

        draw.draw_scatter_3d(pre_a, pre_b, loss) # 注意，loss 与参数 a,b要对应
        draw.draw_contour(pre_a, pre_b)
        draw.draw_regression_curve(optimizer,x,y)
        draw.draw_loss_curve(all_loss, all_step)

        if step % 1 == 0:
            print("step: ", step, " loss: ", loss)
            # plt.show()
            plt.pause(0.01)
    print(all_step)
    print(all_loss)
    plt.show()

