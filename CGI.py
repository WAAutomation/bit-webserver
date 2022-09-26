import os

class CGIProcess:
    def __init__(self, head, body):
        self.body = body.spilt('&')
        self.url = head

    def process(self):
        os.system("python ./cgi-bin/calculator 123 ")


os.system("python ./cgi-bin/calculator.py 123 456")
print(os.popen("python ./cgi-bin/calculator.py 123 456").readlines())