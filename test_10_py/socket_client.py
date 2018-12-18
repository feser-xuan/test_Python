# -*- coding:utf-8 -*-
# @author: Weixuan.Ding
# @time  : 2018/10/15 17:19
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
client = socket.socket()
ip_port = ("127.0.0.1",8888)
client.connect(ip_port)
data = client.recv(1024)
print(data.decode())
while True:
    # data = client.recv(1024)
    # print(data)
    msg_input = input('Please input : ')
    client.send(msg_input.encode())
    if msg_input == 'exit':
        break
    data = client.recv(1024)
    print(data.decode())

