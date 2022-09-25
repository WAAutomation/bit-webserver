class HttpAnalysis:
    def __init__(self):
        # 请求行
        self.method = None          # GET/POST
        self.url = None             # 请求URL
        self.protocol = None        # HTTP版本及协议

        self.header = dict()        # 请求头
        self.body = dict()          # 请求体

        self.Cookie = None
        self.request_data = dict()  # 请求数据
        self.response_line = ''
        self.response_head = dict()  # 请求头
        self.response_body = ''  # 最终请求的html代码

    def request_analyse(self, request):
        """请求报文解析入口"""
        request = request.decode('utf-8')
        request_line, request_rest = request.split('\r\n', 1)
        request_header, request_body = request_rest.split('\r\n\r\n', 1)

        # print("line------")
        # print(request_line)
        # print("header----")
        # print(request_header)
        # print("body------")
        # print(request_body)

        # self.line_analyse(request_line)
        # self.header_analyse(request_header)

    def line_analyse(self, request_line):
        """请求行解析"""
        header_list = request_line.split(' ')
        self.method = header_list[0].upper()
        self.url = header_list[1]
        if self.url == '/':
            self.url = '/index.html'
        self.protocol = header_list[2]

    def header_analyse(self, request_head):
        """请求头解析"""
        head_options = request_head.split('\r\n')
        for option in head_options:
            key, val = option.split(': ', 1)
            self.head[key] = val
        if 'Cookie' in self.head:
            self.Cookie = self.head['Cookie']  # 提取出来Cookie


