import os
import time


# 定义一个LogM类，属性有ip，状态码，用户终端浏览器，请求时间等
class LogM(object):
    def __init__(self, ip, url, status, user_agent, request_file, request_time, request_method):
        self.__ip = ip  # ip
        self.__url = url  # 访问url
        self.__status = status  # 状态码
        self.__user_agent = user_agent  # 用户终端浏览器
        self.__request_file = request_file  # 请求文件
        self.__request_time = request_time  # 请求时间
        self.__request_method = request_method  # 请求方法

    def get_ip(self):
        return self.__ip

    def get_url(self):
        return self.__url

    def get_status(self):
        return self.__status

    def get_user_agent(self):
        return self.__user_agent

    def get_request_file(self):
        return self.__request_file

    def get_request_time(self):
        return self.__request_time

    def get_request_method(self):
        return self.__request_method

    # 产生log文件名
    @staticmethod
    def generate_log_file_name():
        t = time.localtime()
        return time.strftime('%Y-%m-%d', t)

    # 产生log
    def generate_log(self, filepath="log", filename="log.txt"):
        # 日志目录
        log_path = os.path.join(os.getcwd(), filepath)
        # 日志文件路径
        filename = self.generate_log_file_name()
        log_name = os.path.join(log_path, filename)

        # 判断日志是否存在
        if not os.path.exists(log_path):
            os.mkdir(log_path)
            # print(log_path, "已创建")
        elif os.path.exists(log_path) and os.path.exists(log_name):
            pass
            # print(log_name, "已存在")

        # 打开日志
        with open(log_name, "a+") as f:
            # 定义日志格式
            log_format = "{my_ip} -- [{my_request_time}] \"{my_request_method} {my_request_file} HTTP/1.0\" {" \
                         "my_status} {my_url} \"{my_user_agent}\""

            # 生成日志
            query_log = log_format.format(
                my_ip=self.get_ip(),
                my_request_time=self.get_request_time(),
                my_request_method=self.get_request_method(),
                my_request_file=self.get_request_file(),
                my_status=self.get_status(),
                my_url=self.get_url(),
                my_user_agent=self.get_user_agent()
            )

            # 将日志写入文件
            f.write(query_log + "\n")


if __name__ == '__main__':
    log = LogM("1", "2", "3", "4", "5", "6", "7")
    log.generate_log()
