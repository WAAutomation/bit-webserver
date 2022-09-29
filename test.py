import os
import subprocess


def test(ip, port, request_num=500, client_num=100):
    command = f".\\Apache24\\bin\\ab -n {request_num} -c {client_num} http://{ip}:{port}/"
    subprocess.Popen(command)


def main(ip, port, request_num=500, client_num=100):
    command = f".\\Apache24\\bin\\ab -n {request_num} -c {client_num} http://{ip}:{port}/"
    os.system(command)


if __name__ == '__main__':
    main("192.168.43.69", 8888)
