"""
    客户端将一张照片上传到服务端, 上传完成后, 客户端直接关闭套接字退出, 服务端此时也退出即可.
"""
from socket import *

SERVER_ADDR = ("0.0.0.0", 8888)
save_file = "socket_demo03.png"


# 接收图片
def recv_image(conn):
    with open(save_file, "wb") as fw:
        while True:
            # 边接收边写入
            data = conn.recv(1024)
            # 当客户端发送完图片, 程序退出，此时服务端的recv函数会立即结束阻塞, 并返回b""
            if not data:
                break
            fw.write(data)


# 网络搭建
def main():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(SERVER_ADDR)
    sock.listen()
    conn, addr = sock.accept()
    print("connect from:", addr)

    recv_image(conn)  # 接受图片

    conn.close()
    sock.close()


if __name__ == '__main__':
    main()
