# -*- coding:utf-8 -*-
# @author: Weixuan.Ding
# @time  : 2018/10/15 19:27
# @E-mail：weixuanfeser@gmail.com
# @Software: PyCharm
import socket

sk = socket.socket()
ip_port = ('127.0.0.1',9999)
sk.connect(ip_port)
with open('socket_server.py','rb') as f:
    for i in f:
        sk.send(i)
        if sk.recv(1024) != b'success':
            break
sk.send('quit'.encode())


