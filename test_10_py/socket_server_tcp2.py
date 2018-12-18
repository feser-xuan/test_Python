# -*- coding:utf-8 -*-
# @author: Weixuan.Ding
# @time  : 2018/10/15 18:53
# @E-mail：weixuanfeser@gmail.com
# @Software: PyCharm
#非阻塞 模块
import socketserver
import random
class MyServer(socketserver.BaseRequestHandler):
    def setup(self):
        pass

    def handle(self):
        conn = self.request
        msg = 'Hello world!'
        conn.send(msg.encode())

        while True:
            data = conn.recv(1024)
            print(data.decode())
            if data == b'exit':
                break
            conn.send(data)
            conn.send(str(random.randint(1,100)).encode())

    def finish(self):
        pass


if __name__ == '__main__':
    server =  socketserver.ThreadingTCPServer(
        ('127.0.0.1',8888),MyServer)
    server.serve_forever()