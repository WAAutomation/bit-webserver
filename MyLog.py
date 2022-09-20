#coding=UTF-8
import time
import shutil
import os

#定义一个LogM类，属性有ip，URL，状态码，点击后跳转目标，用户终端浏览器
class LogM(object):
    def __init__(request, ip, url, status, hitdes, user_agent):
        request.__ip = ip                  # ip
        request.__url = url                # url
        request.__status = status          # 状态码
        request.__hitdes = hitdes          # 点击后跳转目标
        request.__user_agent = user_agent  # 用户终端浏览器
    def get_ip(request):
        return request.__ip
    def get_url(request):
        return request.__url
    def get_status(request):
        return request.__status
    def get_hitdes(request):
        return request.__hitdes
    def get_user_agent(request):
        return request.__user_agent

# 生成当前时间
def get_timestamp():
    t = time.localtime()
    return time.strftime('%Y-%m-%d %H:%M:%S', t)

# 产生log
def generate_log(filepath="log", filename="log.txt"):
    # 日志目录
    log_path = os.path.join(os.getcwd(), filepath)
    # 日志文件路径
    log_name = os.path.join(log_path, filename)
    # 判断日志是否存在
    if not os.path.exists(log_path):
        os.mkdir(log_path)
        print(log_path, "已创建")
    elif os.path.exists(log_path) and os.path.exists(log_name):
        print(log_name, "已存在")
    # 打开日志
    with open(log_name, "a+") as f:
        # 生成日志
        # 获取当前时间
        time_str = get_timestamp()
        # 定义日志格式
        log_format = "{myip}--{mylocaltime}\t\"GET {myurl} HTTP/1.1\"\t{mystatus}\t{myhitdes}\t{myuseragent}"
        # 日志信息 logm1是一条实例
        query_log = log_format.format(
            ip=logm1.get_ip(),
            mylocaltime=time_str,
            myurl=logm1.get_url(),
            mystatus=logm1.get_status(),
            myreferece=logm1.get_hitdes(),
            myuseragent=logm1.get_useragent()
        )
        # 将日志写入文件
        f.write(query_log + "\n")

if __name__ == '__main__':
    generate_log(filepath="log", filename="log1.txt")

