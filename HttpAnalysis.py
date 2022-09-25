class HttpHeaderAnalysis:
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
        self.session = None

    def passRequestLine(self, request_line):  # 定义method/url/protocol
        header_list = request_line.split(' ')
        self.method = header_list[0].upper()
        self.url = header_list[1]
        if self.url == '/':
            self.url = '/index.html'
        self.protocol = header_list[2]

    def passRequestHead(self, request_head):  # 定义head（字典）
        head_options = request_head.split('\r\n')
        for option in head_options:
            key, val = option.split(': ', 1)
            self.head[key] = val
        if 'Cookie' in self.head:
            self.Cookie = self.head['Cookie']  # 提取出来Cookie

    def passRequest(self, request):  # 解析请求报文入口函数
        request = request.decode('utf-8')
        if len(request.split('\r\n', 1)) != 2:
            return
        request_line, body = request.split('\r\n', 1)
        request_head = body.split('\r\n\r\n', 1)[0]
        self.passRequestLine(request_line)
        self.passRequestHead(request_head)
        # *********************self填充完成***************************