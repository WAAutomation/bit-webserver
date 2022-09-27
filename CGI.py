import os


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
            response_body = f.buffer.read().decode('utf-8')
            response_body_size = '3072'
        return response_body, response_body_size
