# -*- coding:utf-8 -*-
# @author: Weixuan.Ding
# @time  : 2018/10/15 19:28
# @E-mail：weixuanfeser@gmail.com
# @Software: PyCharm
import socket

sk = socket.socket()

ip_port = ('127.0.0.1',9999)

sk.bind(ip_port)
sk.listen(5)
while True:
    conn ,address = sk.accept()
    while True:
        with open('file_recv','ab') as f:
            data = conn.recv(1024)
            if data == b'quit':
                break
            f.write(data)
        conn.send('success'.encode())
sk.close()
