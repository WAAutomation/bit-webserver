import socket
import threading
from concurrent.futures import ThreadPoolExecutor

threadLock = threading.Lock()
max_thread = 20


def process_conn(sock, address):
    print(threading.current_thread())

    recv_data = sock.recv(1024)

    if recv_data:
        # 回送数据到客户端
        threadLock.acquire()  # 同步锁

        print(recv_data)
        #response = "HTTP/1.1 200 OK\r\n\r\n"
        #sock.send(response.encode("utf-8"))
        content=http_content(recv_data)
        sock.send(content.encode("utf-8"))

        threadLock.release()  # 同步锁
    # 5. close socket
    print("close socket..")
    sock.close()


def http_content(recv_data):  # 处理recv_data(解析),返回发送给浏览器的数据
    response = "HTTP/1.1 200 OK\r\n\r\n"
    content = "<h1>First Page</h1>"
    return response+content

def main():
    # 1. create socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. bind local information
    tcp_server_socket.bind(("127.0.0.1", 8888))
    # 3. listen request
    tcp_server_socket.listen()
    pool = ThreadPoolExecutor(max_thread)
    # 4. accept connection from client

    while True:
        print(threading.current_thread())
        print("waiting ........")
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("deal with connection ....")
        # t = threading.Thread(target=process_conn, args=(new_client_socket, client_addr))
        # t.start()
        pool.submit(process_conn, new_client_socket, client_addr)


if __name__ == '__main__':
    main()