# -*- coding:utf-8 -*-
# @author: Weixuan.Ding
# @time  : 2018/10/21 17:48
# @E-mail：weixuanfeser@gmail.com
# @Software: PyCharm

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# data = pd.read_csv('config/train.csv')
Xn = pd.read_csv('config/train.csv',usecols=[1]).values
Yn = pd.read_csv('config/train.csv',usecols=[2]).values
kmeans = KMeans().fit(X=Xn,y=Yn)
print(kmeans.cluster_centers_)
print(kmeans.labels_)