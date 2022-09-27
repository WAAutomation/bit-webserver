import os


class CGIProcess:
    def __init__(self, url, body):
        self.url = url
        self.body = body.split('\r\n')[0:-1]
        print(self.body)

    def process(self):
        command = "python ." + self.url
        for arg in self.body:
            arg = arg.split('=')
            command += f' {arg[-1]}'
        with os.popen(command) as f:
            response = f.buffer.read().decode('utf-8')
        return response
