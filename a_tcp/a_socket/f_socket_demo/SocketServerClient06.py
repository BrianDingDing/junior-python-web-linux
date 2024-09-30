from socket import *
from time import sleep

upload_file = "upload_06.png"
SERVER_ADDR = ("127.0.0.1", 8888)


def send_image(sock):
    with open(upload_file, "rb") as fr:
        while True:
            data = fr.read(1024)
            if not data:
                break
            sock.send(data)

    # 防止图片最后的一次发送与##产生粘连. 可以通过发送延迟, 防止粘包.
    sleep(0.1)
    sock.send(b"##")  # 表示文件发送完成

    msg = sock.recv(1024)
    print(msg.decode())


def main():
    sock = socket()
    sock.connect(SERVER_ADDR)
    send_image(sock)
    sock.close()


if __name__ == '__main__':
    main()
