# -*- coding: utf-8 -*-
"""
==============================================================================
Time : 2021/7/10 7:10 下午
Author : Dufy
Email : 813540660@qq.com
File : test.py


==============================================================================
"""

# 布丰投针试验

"""
布丰投针试验：
针长a, 线间距d, a<d
针中点M 到最近的线距离为：x∈[0，d/2]
针与线的夹角为 alpha ∈[0,pi]

相交条件：x<a*sin(alpha)/2
"""

import numpy as np
def throw_needle(n, a, d=1):
    """

    :param n: 投针次数
    :param a: 针长度
    :param d: 1
    :return: pi 的估计值
    """
    alpha = np.random.uniform(0, np.pi, n)
    x = np.random.uniform(0, d/2, n)
    m = np.sum(x < a*np.sin(alpha)/2)
    pi = 2*a*n/d/m
    return pi


prob = throw_needle(10**8, 0.8)
print(prob)

