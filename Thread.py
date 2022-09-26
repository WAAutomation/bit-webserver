from HttpAnalysis import HttpAnalysis
from HttpResponse import HttpResponse
from MyLog import LogM

class Thread:
    def __init__(self, socket):
        self.thread_socket = socket
        self.http_analysis = HttpAnalysis()
        self.http_response = HttpResponse()

    def run(self):
        """"进程运行"""
        request = self.thread_socket.recv(1024)
        print(request)

        self.http_analysis.request_analyse(request)

        if self.http_analysis.method == "GET":
            response = self.http_response.response_generate(self.http_analysis.url, 'GET')
        elif self.http_analysis.method == "POST":
            pass
        elif self.http_analysis.method == "HEAD":
            response = self.http_response.response_generate(self.http_analysis.url, 'HEAD')
        else:
            pass

        log = LogM(self.http_analysis.header['Host'], self.http_analysis.header['Host'] + self.http_analysis.url, self.http_response.response_code, self.http_analysis.header['User-Agent'], self.http_analysis.url, self.http_analysis.request_time, self.http_analysis.method)
        log.generate_log()
        # response = self.response_test1()

        self.thread_socket.send(response.encode("utf-8"))

    def interrupt(self):
        """"进程中断"""
        self.thread_socket.close()

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
