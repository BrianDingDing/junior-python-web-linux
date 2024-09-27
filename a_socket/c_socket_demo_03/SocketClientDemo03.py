from socket import *

upload_file = "upload_03.png"
SERVER_ADDR = ("127.0.0.1", 8888)


# 发送图片
def send_image(sock):
    with open(upload_file, "rb") as fr:
        while True:
            # 边读取边发送
            data = fr.read(1024)
            if not data:
                break
            sock.send(data)


# 网络搭建
def main():
    sock = socket()
    sock.connect(SERVER_ADDR)
    send_image(sock)  # 发送图片
    sock.close()


if __name__ == '__main__':
    main()
