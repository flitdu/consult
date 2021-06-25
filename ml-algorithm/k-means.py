# -*- coding: utf-8 -*-
"""
@Time : 2021/6/24 12:16 上午
@Author : Dufy
@Email : 813540660@qq.com
@File : k-means.py
@Software: PyCharm 
Description :
1) 参考 西瓜书 P203
2) 扩展：文本聚类，搜索github
3）k 值如何定？？

"""
import pandas as pd
import numpy as np

data_watermelon = "../data/西瓜数据集4.0.txt"
def load_data(path):
    df = pd.read_csv(data_watermelon, sep='\t')
    return df.loc[:,['density','sugar']].values  # 转numpy

class KMeans:
    def __init__(self, path, k=2):
        self.k = k
        self.data = load_data(path)
        self.centroid = [[0,0] for _ in range(k)]

    # def update_cen



if __name__ == "__main__":
    pass


    k_means = KMeans(data_watermelon, 4)
    print(k_means.k)
    print(k_means.centroid)
    print(k_means.data)
