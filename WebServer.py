import socket


class WebServer:
    def __init__(self, ip="127.0.0.1", port=8888, max_connect=128):
        self.port = port
        self.ip = ip
        self.max_connect = max_connect
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def open(self):
        """开启服务器连接"""
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定
        self.server_socket.bind((self.ip, self.port))
        # 监听
        self.server_socket.listen(self.max_connect)

        while True:
            # 等待新客户端的连接
            new_socket, client_addr = self.server_socket.accept()
            self.response_test(new_socket)

    def close(self):
        """关闭服务器连接"""
        self.server_scoket.close()

    @staticmethod
    def response_test(new_socket):
        """为这个客户返回数据"""
        #  1.接收浏览器发送过来的请求，即HTTP请求
        #  GET / HTTP/1.1
        request = new_socket.recv(1024)
        print(request)

        #  2.返回HTTP格式的数据，给浏览器
        #  准备发送的header
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"  # header与body之间必须隔一行
        #  准备发送的body
        response += "<h1>Welcome<h1>"
        new_socket.send(response.encode("utf-8"))

        new_socket.close()


if __name__ == '__main__':
    web_server = WebServer("127.0.0.1", 8888, 128)
    web_server.open()
    web_server.close()
