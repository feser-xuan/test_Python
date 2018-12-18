# -*- coding:utf-8 -*-
# @author: Weixuan.Ding
# @time  : 2018/10/12 17:19
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
#import time
#import time as t
#from time import time,localtime
# from time import *
#
# print localtime()
# print time()

# print t.time()
# print t.clock()
# print time.localtime()

# import m1
#
# m1.printdata('data:123')

# a = True
#
# while a:
#     b = input('type something:')
#     print b
#     if b == 1:
#         a = False
#     else:
#         pass
#     print ("still in while !")
# print ('Finish run')
# try:
#     file = open('eee.txt','r+')
# except Exception as e:
#     print 'do not find this file'
#     response = raw_input('do you want to creat a new file(y/n)?\n:')
#     print response
#
#     if response == 'y':
#         file = open('eee.txt','w')
#     else:
#         pass
# else:
#     file.write('sss')
# file.close()
#组合
# a = [1,2,3]
# b = [4,5,6]
# print zip(a,b)
# print list(zip(a,b))
#
# for i,j in zip(a,b):
#     print i/2,j/2

# import copy
#
# a = [1,2,3]
# b = a
#
# print 'id a:',id(a)
# print 'id b:',id(b)
# print 'a:',a,'b:',b

import pickle

a = {'da':111,2:[23,1,4],'23':{1:2,'d':'sad'}}

# file = open('pickle_examle.pickle','wb')
# pickle.dump(a,file)
# file.close()

# with open('pickle_examle','rb') as file:
# #file = open('pickle_examle.pickle','rb')
# a_dict = pickle.load(file)
# #file.close()
#
# print a_dict

# char_list = ['a','b','c','c','d','d','d']
# print set(char_list)
# sentence = 'Welcome Back to This Tutorrial'
#
# unique_char = set(sentence)
# unique_char.remove('c')
#
# print unique_char

# Regular Expression 正则表达式

import re

# pattern1 = 'cat'
# pattern2 = 'bird'
#
# string = 'dog runs to cat '
#
# print pattern1 in string
# print pattern2 in string
#
# print re.search(pattern1,string)
# print re.search(pattern2,string)
#
# ptn = r'r[au]n'
# print re.search(ptn,'dog rans to cat')

# print re.search(r'r[0-9]n','dog r3ns to cat')
# print re.search(r'r[a-z]n','dog rans to cat')
# print re.search(r'r[0-9a-z]n','dog rans to cat')
#
# print re.search(r'r\dn','dog rans to cat r4n')
# print re.search(r'r\Dn','dog rans to cat r4n')
#
# print re.search(r'a+','aaaaaaaaaaa')

# match = re.search(r'(\d+),Data: (.+)','ID: 001234, Data: Oct/12/2018')
# print match.group()
# print match.group(1)
# print match.group(2)

# More Threading

# import threading
# import time
# def thread_job():
#     print 'This is an addend Thread,number is %s'%threading.current_thread()
#     print 'T1 start\n'
#     for i in range(10):
#         time.sleep(0.5)
#     print 'T1 finish\n'
#
# def T2_job():
#     print 'T2 start\n'
#     print 'T2 finish\n'
# def main():
#     thread_add = threading.Thread(target=thread_job)
#     thread2 = threading.Thread(target=T2_job)
#     thread_add.start()
#     thread2.start()
#
#     thread_add.join()
#     print 'all done\n'
#     # print threading.active_count()
#     # print threading.enumerate()
#     # print threading.current_thread()
#
#
# if __name__ == '__main__':
#     main()

# import threading
# import time
# from Queue import Queue
#
#
# def job(l,q):
#     for i in range(len(l)):
#         l[i] = l[i]**2
#     q.put(l)
#
# def multithreading():
#     q = Queue()
#     threads = []
#     data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
#     for i in range(4):
#         t = threading.Thread(target=job,args=(data[i],q))
#         t.start()
#         threads.append(t)
#     for thread in threads:
#         thread.join()
#
#     results = []
#     for _ in range(4):
#         results.append(q.get())
#     print results
#
# if __name__ == '__main__':
#     multithreading()

import threading

def job1():
    global A,lock
    lock.acquire()
    for i in range(10):
        A += 1
        print 'job1',A
    lock.release()
def job2():
    global A,lock
    lock.acquire()
    for i in range(10):
        A += 10
        print 'job2',A
    lock.release()
if __name__ == '__main__':
    lock = threading.Lock()
    A = 0
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
