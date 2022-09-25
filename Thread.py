import socket


class Thread:
    def __init__(self, socket):
        self.socket = socket

    def run(self):
        request = self.socket.recv(1024)
        print(request)
        # 准备发送的header
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"  # header与body之间必须隔一行
        # 准备发送的body
        response += "<h1>Welcome<h1>"
        self.socket.send(response.encode("utf-8"))

    def interrupt(self):
        """"进程中断"""
        self.socket.close()
