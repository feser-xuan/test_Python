# -*- coding:utf-8 -*-
# @author: Weixuan.Ding
# @time  : 2018/10/15 18:44
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


import socket
sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_port = ('127.0.0.1',8888)
while True:
    msg = input('Please input : ')
    if msg == 'exit':
        break
    sk.sendto(msg.encode(),ip_port)

sk.close()