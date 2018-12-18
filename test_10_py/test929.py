# -*- coding:utf-8 -*-
# author: Weixuan.Ding
# time  : 2018/9/29

# 函数 print calendar

# def is_leap_year(year):
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         return True
#     else:
#         return False
#
# def get_num_of_days_in_mouth(year,mouth):
#     if mouth in (1,3,5,7,8,10,12):
#         return 31
#     elif mouth in (4,6,9,11):
#         return 30
#     elif is_leap_year(year):
#         return 29
#     else:
#         return 28
#
# def get_total_num_of_day(year,mouth):
#     days = 0
#     for y in range(1800,year):
#         if is_leap_year(y):
#             days += 366
#         else:
#             days += 365
#     for m in range(1,mouth):
#         days += get_num_of_days_in_mouth(year,m)
#     return days
#
# def get_start_day(year,mouth):
#     return (3 + get_total_num_of_day(year,mouth)) % 7
#
# print get_start_day(2033,12)

# 函数 递归
#
# def p(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * p(n - 1)
#
# print p(3)

# 斐波那契数列

# def fib(n):
#     if n == 1 or n ==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
#
# print fib(20)

# 汉诺塔 问题
# count = 0
# def hanoi(n,A,B,C):
#     global count
#     if n == 1:
#         print 'Move' ,n,'from',A,'to' ,C
#         count += 1;
#     else:
#         hanoi(n - 1,A ,C ,B)
#         print 'Move', n,'from', A, 'to',C
#         count +=1;
#         hanoi(n - 1,B ,A , C)
#
# hanoi(5 ,'Left', 'Mid', "Right")
# print count


# 停车问题
# import random
# def parking(low,high):
#     if high - low < 1:
#         return 0
#     else:
#         x = random.uniform(low, high - 1)
#         return parking(low ,x) + 1 + parking(x + 1, high)
# s = 0.0
# for i in range(100000):
#     s += parking(0,5)
# print s / 100000

# 字符串

# print len("Michael")
# print 'first_name' + 'jordan'
#
# my_str = 'michael Jordan'
# for c in my_str:
#     print c

# def vowles_count(s):
#     count = 0
#     for c in s:
#         if c in 'aeiouAEIOU':
#             count += 1
#     return count
# print vowles_count('hello world')

# 人名游戏

f = open('names.txt','r')

def is_panindrom_rec(name):
    if len(name) <= 1:
        return  True
    else:
        if name[0] != name[-1]:
            return False
        else:
            return is_panindrom_rec(name[1:-1])

def is_panlindrom(name):
    low = 0
    high =  len(name) - 1

    while low < high:
        if name[low] != name[high]:
            return False
        low += 1
        high -= 1

    return True

def is_ascending(name):
    p = name[0]

    for c in name:
        if p > c:
            return False
        p = c
    return True

import re



for line in f:
    line = line.strip()  #去掉回车
    pattern = 'M.M'
    result = re.search(pattern,line)
    if result:
        print 'Name is {}'.format(line)

f.close()







