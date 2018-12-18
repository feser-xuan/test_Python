# -*- coding:utf-8 -*-
# @author: Weixuan.Ding
# @time  : 2018/10/10 20:01
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
# file = open('my_file.txt','r')
#
# #print content
#
# # for i in file:
# #     print i
# print file.readlines()
# file.close()

# class
from optparse import OptionParser
class Calculator:
    name = 'Good calculator'
    price = 18

    def __init__(self,name ,price ,hight ,witdth ,weight):
        # self.name = name
        # self.price = price
        self.h = hight
        self.wi = witdth
        self.we = weight
    def add(self,x,y):
        print self.name
        result = x + y
        print result

    def minus(self,x,y):
        result = x - y
        print result
    def times(self,x,y):
        print x * y
    def divide(self,x,y):
        print x / y

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-h','--help',action='')
    culat = Calculator('Good calculator',12,30,19,90)

    culat.add(1,1)



