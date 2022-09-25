class HttpResponse:
    def __init__(self):
        self.html_path = "./page"

        self.response_line = None
        self.response_header = dict()
        self.response_split = '\r\n'
        self.response_body = ""

    def line_generate(self, code):
        if code == 200:
            self.response_line = Code.OK
        elif code == 400:
            self.response_line = Code.BAD_REQUEST
        elif code == 403:
            self.response_line = Code.FORBIDDEN
        elif code == 404:
            self.response_body = Code.NOT_FOUND

    def header_generate(self, url):
        context_type = url.split('.', 1)[1]

        if context_type == "html":
            self.response_header['Content-Type'] = 'text/html'
        elif context_type == "css":
            self.response_header['Content-Type'] = 'text/css'

    def get_header(self):
        header = ""

        header += 'Content-Type: '
        header += self.response_header['Content-Type']
        header += self.response_split

        return header

    def response_generate(self, url):
        html_url = self.html_path + url
        try:
            # 尝试打开html文件，准备body
            f = open(html_url, 'r', encoding="utf-8")
        except IOError as error:
            self.line_generate(404)
        else:
            self.line_generate(200)
            self.header_generate(url)

            self.response_body = f.read()
            f.close()

        return self.response_line + self.get_header() + self.response_split + self.response_body


class Code:
    OK = "HTTP/1.1 200 OK\r\n"
    BAD_REQUEST = "HTTP/1.1 400 Bad Request\r\n"
    FORBIDDEN = "HTTP/1.1 403 Forbidden\r\n"
    NOT_FOUND = "HTTP/1.1 404 Not Found\r\n"
