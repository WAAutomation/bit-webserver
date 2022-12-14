import time


class HttpAnalysis:
    def __init__(self):
        # 请求行
        self.method = None          # GET/POST/HEAD
        self.url = None             # 请求URL
        self.protocol = None        # HTTP版本及协议

        self.header = dict()        # 请求头
        self.body = None            # 请求体

        # 其他
        self.request_time = None    # 请求时间

    def request_analyse(self, request):
        """
        请求报文解析入口
        
        Args:
            request: http request message

        Returns:

        """
        request = request.decode('utf-8')
        # print(request)

        request_line, request_rest = request.split('\r\n', 1)
        request_header, request_body = request_rest.split('\r\n\r\n', 1)

        # print("line------")
        # print(request_line)
        # print("header----")
        # print(request_header)
        # print("body------")
        # print(request_body)

        self.request_time = time.strftime("%d/%a/%Y %H:%M:%S GMT", time.localtime())

        self.line_analyse(request_line)
        self.header_analyse(request_header)
        self.body = request_body

    def line_analyse(self, request_line):
        """
        请求行解析

        Args:
            request_line: line of http request message

        Returns:

        """
        header_list = request_line.split(' ')
        self.method = header_list[0].upper()
        self.url = header_list[1]
        if self.url == '/':
            self.url = '/index.html'
        self.protocol = header_list[2]

    def header_analyse(self, request_head):
        """
        请求头解析

        Args:
            request_head: head of http request message

        Returns:

        """
        head_options = request_head.split('\r\n')
        for option in head_options:
            key, val = option.split(': ', 1)
            self.header[key] = val
