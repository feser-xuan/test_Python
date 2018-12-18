# -*- coding:utf-8 -*-
# @author: Weixuan.Ding
# @time  : 2018/11/23 19:42
# @E-mail：weixuanfeser@gmail.com
# @Software: PyCharm
# def ip_to_int(s):
#     L = '0b' + ''.join([bin(int(i)) for i in s.split('.')]).replace('0b', '')
#     print(L)
#     print(int(L, 2))
#
#
# if __name__ == '__main__':
#     s = "10.3.9.12"
#     ip_to_int(s)
import time
import datetime


def utc2local(utc_st):
    # “”“UTC时间转本地时间（+8:00）”“”
    now_stamp = time.time()
    local_time = datetime.datetime.fromtimestamp(now_stamp)
    utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    local_st = utc_st + offset
    return local_st

def local2utc(local_st):
    # “”“本地时间转UTC时间（-8:00）”“”
    time_struct = time.mktime(local_st.timetuple())
    utc_st = datetime.datetime.utcfromtimestamp(time_struct)
    return utc_st
if __name__ == '__main__':
    utc_time = datetime.datetime(2014, 9, 18, 10, 42, 16, 126000)

    # utc转本地
    local_time = utc2local(datetime.datetime.fromtimestamp(time.time()))
    print(local_time.strftime('%Y-%m-%d %H:%M:%S'))
    # output：2014-09-18 18:42:16


    # 本地转utc
    utc_tran = local2utc(datetime.datetime.fromtimestamp(time.time()))
    print(utc_tran.strftime('%Y-%m-%d %H:%M:%S'))
