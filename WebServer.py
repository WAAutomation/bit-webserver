import socket
import threading
from concurrent.futures import ThreadPoolExecutor
from Thread import Thread
from test import test


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
        """
        向线程池加入新线程

        Args:
            new_socket: new socket
            client_addr: client address

        Returns:

        """
        self.thread_pool.submit(self.run_thread, new_socket, client_addr)

    @staticmethod
    def run_thread(new_socket, client_addr):
        """
        线程运行

        Args:
            new_socket: new socket
            client_addr: client address

        Returns:

        """
        # 打开同步锁
        lock = threading.Lock()
        # threading.Lock().acquire()

        # 创建并运行thread
        with lock:
            new_thread = Thread(new_socket, client_addr)
            new_thread.run()

        # 关闭同步锁
        # threading.Lock().release()

        # bug-线程中断时间不确定
        new_thread.interrupt()

    def close(self):
        """关闭服务器连接"""
        self.server_socket.close()


if __name__ == '__main__':
    ip = "127.0.0.1"
    port = 8888
    web_server = WebServer(ip, port, 128)
    test(ip, port, 500, 200)
    web_server.open()
    web_server.close()
