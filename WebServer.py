import socket
import threading
from concurrent.futures import ThreadPoolExecutor
from Thread import Thread


class WebServer:
    def __init__(self, ip="127.0.0.1", port=8888, max_connect=128):
        self.ip = ip
        self.port = port
        self.max_connect = max_connect
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.thread_pool = ThreadPoolExecutor(self.max_connect)

    def open(self):
        """开启服务器连接"""
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 绑定
        self.server_socket.bind((self.ip, self.port))
        # 监听
        self.server_socket.listen(self.max_connect)

        # 等待新客户端的连接
        while True:
            new_socket, client_addr = self.server_socket.accept()
            self.insert_new_thread(new_socket, client_addr)
            # self.response_test2(new_socket)

    def insert_new_thread(self, new_socket, client_addr):
        self.thread_pool.submit(self.run_thread, new_socket, client_addr)

    def run_thread(self, new_socket, client_addr):
        # 打开同步锁
        threading.Lock().acquire()

        # 创建并运行thread
        new_thread = Thread(new_socket)
        new_thread.run()

        # 关闭同步锁
        threading.Lock().release()

        # bug-线程中断时间不确定
        new_thread.interrupt()

    def close(self):
        """关闭服务器连接"""
        self.server_socket.close()

    @staticmethod
    def response_test1():
        """返回简单静态网页（测试用）"""
        # 准备发送的header
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"  # header与body之间必须隔一行
        # 准备发送的body
        response += "<h1>Welcome<h1>"

        return response

    @staticmethod
    def response_test2():
        """返回复杂静态网页（测试用）"""
        file_name1 = "/error.html"
        file_name2 = "/style.css"

        try:
            #  准备发送的body，打开HTML文件
            f1 = open("page" + file_name1, 'rb')
            f2 = open("page" + file_name2, 'rb')
        except IOError as error:
            response = "HTTP/1.1 404 NOT FOUND\r\n"
            response += '\r\n'
            response += "----file not found----"
        else:
            html_content = f1.read()
            html_content += f2.read()
            f1.close()
            f2.close()
            #  准备发送的header
            response = "HTTP/1.1 200 OK\r\n"
            response += "\r\n"  # header与body之间必须隔一行
            # response += html_content
            print(response)

        return response


if __name__ == '__main__':
    web_server = WebServer("127.0.0.1", 8888, 128)
    web_server.open()
    web_server.close()
