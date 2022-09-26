import os
import time
import pathlib


class HttpResponse:
    def __init__(self):
        self.html_path = "./page"

        self.response_line = None
        self.response_header_key = ["Server", "Date", "Content-Type", "Connection", "Content-Length"]
        self.response_header = dict()
        self.response_split = '\r\n'
        self.response_body = ""

    def line_generate(self, code):
        """

        Args:
            code: status code

        Returns:

        """
        if code == 200:
            self.response_line = Code.OK
        elif code == 400:
            self.response_line = Code.BAD_REQUEST
        elif code == 403:
            self.response_line = Code.FORBIDDEN
        elif code == 404:
            self.response_line = Code.NOT_FOUND

    def header_generate(self, url):
        """

        Args:
            url: relative url of file

        Returns:

        """

        self.response_header['Server'] = 'BIT-WS/1.0'
        self.response_header['Date'] = time.strftime("%a, %b %d %Y %H:%M:%S GMT", time.localtime())

        context_type = url.split('.', 1)[1]

        if context_type == "html":
            self.response_header['Content-Type'] = 'text/html'
        elif context_type == "css":
            self.response_header['Content-Type'] = 'text/css'

        self.response_header['Connection'] = 'Close'

    def get_header(self):
        """

        Returns: header in string type

        """
        header = ""

        for item in self.response_header_key:
            if item in self.response_header.keys():
                header += item
                header += ': '
                header += self.response_header[item]
                header += self.response_split
        # header += 'Content-Type: '
        # header += self.response_header['Content-Type']
        # header += self.response_split

        # print(header)
        return header

    def response_generate(self, url):
        """

        Args:
            url: relative url of file

        Returns: http response

        """
        html_url = self.html_path + url
        path = pathlib.Path(html_url)

        if not path.exists():
            # 404
            self.line_generate(404)
            url = "/404.html"
            html_url = self.html_path + url
        else:
            # 200
            self.line_generate(200)

        self.response_header['Content-Length'] = str(os.path.getsize(html_url))
        self.header_generate(url)

        # 尝试打开html文件，准备body
        f = open(html_url, 'r', encoding="utf-8")
        self.response_body = f.read()
        f.close()

        return self.response_line + self.get_header() + self.response_split + self.response_body


class Code:
    OK = "HTTP/1.0 200 OK\r\n"
    BAD_REQUEST = "HTTP/1.0 400 Bad Request\r\n"
    FORBIDDEN = "HTTP/1.0 403 Forbidden\r\n"
    NOT_FOUND = "HTTP/1.0 404 Not Found\r\n"
