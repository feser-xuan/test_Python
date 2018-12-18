# -*- coding:utf-8 -*-
# author: Weixuan.Ding
# time  : 2018/9/28

# points = int(raw_input('Leading points: '))
# has_ball = raw_input('The leading team has ball (yes/no)')
# seconds = int(raw_input('The remaining seconds: '))
#
# points -= 3
#
# if has_ball == 'yes':
#     points += 0.5
# else:
#     points -= 0.5
#
# if points < 0:
#     points = 0
#
# points **= 2
#
# if points > seconds:
#     print 'Safe'
# else:
#     print 'Not safe'

# test -- while

# count = 0
#
# while count < 10:
#     print count
#     count += 1

# import sys,logging,logging.handlers
#
# reload(sys)
# sys.setdefaultencoding('utf-8')
#
# logging.basicConfig(level=logging.DEBUG,
#                     format="%(asctime)s %(name)s %(levelname)s %(message)s",
#                     datefmt = '%Y-%m-%d  %H:%M:%S %a'    #注意月份和天数不要搞乱了，这里的格式化符与time模块相同
#                     )
# logging = logging.getLogger("")
#
# logging.debug("msg1")
# logging.info("msg2")
# logging.warning("msg3")
# logging.error("msg4")
# logging.critical("msg5")

# import math
# e = 1
#
# for i in range(1,10):
#     e += 1.0 / math.factorial(i)
#
# print e
# n = 6
#
# while n != 1:
#     if n % 2 == 0:
#         n /= 2
#     else:
#         n = 3 * n + 1
#     print n

# for i in range(1,10):
#     for j in range(1,10):
#         print format(i * j,'3d'),
#     print

# for c in range(35 + 1):
#     for r in range(36):
#         if 2 * c + 4 * r == 94 and c + r == 35:
#             print c , r

# x = 0
#
# low = 0
# high = x
#
# guss = (low + high) / 2
#
# while abs(guss ** 2 - x) > 1e-4:
#     if guss ** 2 > x:
#         high = guss
#     else:
#         low = guss
#
#     guss = (low + high) / 2
# print  guss

# 素数
# import math
#
# count = 0
# num = 2
# x = 2
# while count < 50:
#     for i in range(2,x):
#         if x % i == 0:
#             #print 'x is not a prime!'
#             break
#     else:
#         print x,' is a prime!'
#         count += 1
#     x += 1

# 回文数

# num = 12321
# num_p = 0
# num_t = num
# while num != 0:
#     num_p = num % 10 + num_p * 10
#     num  = num / 10
#
# if num_t == num_p:
#     print 'ok'
# else:
#     print num_p,num_t
#     print 'no'

# 回文数 + 素数(问题)
#
# num = 123321
# num_p = 0
# num_t = num
#
# is_palin = False
# is_prime = False
#
# while num != 0:
#     num_p = num % 10 + num_p * 10
#     num  = num / 10
#
# if num_t == num_p:
#     is_palin = True
# else:
#     print num_p,num_t
#     print 'no'
#
# for i in range(2,num):
#     if num % i == 0:
#         break
# else:
#     is_prime = True
#
# if is_prime and is_palin:
#     print 'ok'
# else:
#     print 'no'

# # 函数
#
# num = 151
#
# def is_palin(num):
#     num_p = 0
#     num_t = num
#     while num_t != 0:
#         num_p = num_p * 10 + num_t % 10
#         num_t = num_t / 10
#     if num == num_p:
#         return True
#     else:
#         return False
#
# def is_prime(num):
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#     return True
#
# if is_palin(num) and is_prime(num):
#     print 'ok'
# else:
#     print 'no'











