import os
import sys


class CGIProcess:
    def __init__(self, url, body):
        self.url = url
        self.body = body.split('\r\n')[0:-1]
        # print(self.body)

    def process(self):
        command = "python ." + self.url
        for arg in self.body:
            arg = arg.split('=')
            command += f' {arg[-1]}'
        with os.popen(command) as f:
            response_body = f.buffer.read()
            response_body_size = len(response_body)
            response_body = response_body.decode('utf-8')
        return response_body, response_body_size


if __name__ == '__main__':
    cgi_process = CGIProcess('/cgi-bin/query.py', 'student_id=100\r\n')
    cgi_process.process()
