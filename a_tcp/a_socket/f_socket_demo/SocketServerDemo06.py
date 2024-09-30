"""
    在上传图片基础上添加一个功能, 当图片上传完毕后, 服务端给客户都安发送一个通知"上传成功", 客户端接收到通知并打印后再退出.
"""
from socket import *

SERVER_ADDR = ("0.0.0.0", 8888)
save_file = "socket_demo06.png"


def recv_image(conn):
    with open(save_file, "wb") as fw:
        while True:
            data = conn.recv(1024)
            if data == b"##":
                break
            fw.write(data)

    conn.send("上传成功".encode())


def main():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(SERVER_ADDR)
    sock.listen()
    conn, addr = sock.accept()
    print("connect from:", addr)

    recv_image(conn)

    conn.close()
    sock.close()


if __name__ == '__main__':
    main()
