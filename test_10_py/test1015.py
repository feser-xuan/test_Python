# -*- coding:utf-8 -*-
# @author: Weixuan.Ding
# @time  : 2018/10/15 11:09
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
# from sklearn import datasets
# from sklearn.linear_model import LinearRegression
#
# loaded_data = datasets.load_boston()
# data_x = loaded_data.data
# data_y = loaded_data.data
#
# model = LinearRegression()
# model.fit(data_x,data_y)
#
# # print (model.predict(data_x[:4,:]))
# # print (data_y[:4])
#
# # print (model.coef_)
# # print (model.intercept_)
# # print (model.get_params())
# print (model.score(data_x,data_y))




# from sklearn import preprocessing
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.datasets.samples_generator import make_classification
# from sklearn.svm import SVC
# import matplotlib.pyplot as plt
#
# # a = np.array([[10,2.7,3.6],
# #               [-100,5,-2],
# #               [120,20,40]])
# # print (a)
# # print (preprocessing.scale(a))
# x,y = make_classification(n_samples=300,
#                           n_features=2,
#                           n_redundant=0,
#                           n_informative=2,
#                           random_state=22,
#                           n_clusters_per_class=1,
#                           scale=100)
# # plt.scatter(x[:,0],x[:,1],c=y)
# # plt.show()
#
# x = preprocessing.scale(x)
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.3)
# clf = SVC()
# clf.fit(x_train,y_train)
# #####################################################
# # print (clf.score(x_test,y_test))
#
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.model_selection import cross_val_score
# from sklearn.neighbors import KNeighborsClassifier
#
# iris = load_iris()
# x = iris.data
# y = iris.target
#
# x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=4)
# # knn = KNeighborsClassifier(n_neighbors=5)
# # knn.fit(x_train,y_train)
# # print (knn.score(x_test,y_test))
#
# kn = KNeighborsClassifier(n_neighbors=15)
# scores = cross_val_score(kn,x,y,cv=10,scoring='accuracy')
# print (scores.mean())

##################################################################
# from sklearn.model_selection import learning_curve
# from sklearn.datasets import load_digits
# from sklearn.svm import SVC
# import matplotlib.pyplot as plt
# import numpy as np
#
# digits = load_digits()
# x = digits.data
# y = digits.target
# train_sizes,train_loss,test_loss = learning_curve(
#     SVC(gamma=0.001),x,y,cv=10,scoring='mean_squared_error',
#     train_sizes=[0.1,0.25,0.5,0.75,1])
# train_loss_mean = -np.mean(train_loss,axis=1)
# test_loss_mean = -np.mean(test_loss,axis=1)
#
# plt.plot(train_sizes,train_loss_mean,'o-',color='r',
#          label='Training')
# plt.plot(train_sizes,test_loss_mean,'o-',color='g',
#          label='Cross-validation')
# plt.xlabel('Training example')
# plt.ylabel('Loss')
# plt.legend(loc='best')
# plt.show()

#############################

from sklearn import svm
from  sklearn import datasets

clf = svm.SVC()
iris = datasets.load_iris()
x , y = iris.data,iris.target
clf.fit(x,y)

#method 1 : pickle
# import pickle
# # with open('save/clf.pickle','wb') as f:
# #     pickle.dump(clf,f)
#
# with open('save/clf.pickle','rb') as f:
#     clf2 = pickle.load(f)
#     print (clf2.predict(x[0:1]))

# method 2 : joblib
from sklearn.externals import joblib
#Save
joblib.dump(clf,'save/clf.pkl')
#resitore
clf3 = joblib.load('save/clf.pkl')
print (clf3.predict(x[0:1]))




