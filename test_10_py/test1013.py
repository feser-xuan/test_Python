# -*- coding:utf-8 -*-
# @author: Weixuan.Ding
# @time  : 2018/10/13 11:27
# @E-mail：weixuanfeser@gmail.com
# @Software: PyCharm
"""
code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
┏┓ ┏┓
┏┛┻━━━┛┻┓
┃ ☃ ┃
┃ ┳┛ ┗┳ ┃
┃ ┻ ┃
┗━┓ ┏━┛
┃ ┗━━━┓
┃ 神兽保佑 ┣┓
┃　永无BUG！ ┏┛
┗┓┓┏━┳┓┏┛
┃┫┫ ┃┫┫
┗┻┛ ┗┻┛
 """
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

# print (iris_X[:2,:])
# print (iris_y)

x_train,x_test,y_train,y_test = train_test_split(iris_X,iris_y,test_size=0.3)
# print (y_train)

knn = KNeighborsClassifier()
knn.fit(x_train,y_train)
print (knn.predict(x_test))
print (y_test)


