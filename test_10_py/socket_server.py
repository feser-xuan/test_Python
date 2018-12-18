# -*- coding:utf-8 -*-
# @author: Weixuan.Ding
# @time  : 2018/10/15 16:51
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
import random
sk = socket.socket()
ip_port = ("127.0.0.1", 8888)
sk.bind(ip_port)
sk.listen(5)
while True:
    print('listening ......')
    conn, address = sk.accept()
    msg = 'connect successfully!'
    conn.send(msg.encode())
    while True:
        data = conn.recv(1024)
        print(data.decode())
        if data == b'exit':
            break
        conn.send(data)
        conn.send(str(random.randint(1,100)).encode())
    conn.close()



