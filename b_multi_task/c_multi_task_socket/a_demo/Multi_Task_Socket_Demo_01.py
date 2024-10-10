"""
    基于多线程的TCP网络并发模型
"""
from multiprocessing import Process
from socket import socket


# 构建网络流程
def main(host="127.0.0.1", port=8888):
    # 创建套接字
    sock = socket()
    sock.bind((host, port))
    sock.listen()
    print("Listen the port %d" % port)

    # 循环等待客户端连接
    while True:
        try:
            conn, addr = sock.accept()
            print(f"Connect from: {addr}")
        except KeyboardInterrupt:
            sock.close()
            break

        # 为连接进来的客户创建新进程
        Process(target=handler, args=(conn,), daemon=True).start()


# 具体处理客户端各种请求
def handler(conn):
    while True:
        data = conn.recv(1024)
        if not data or data == b'##':
            break
        print(data.decode())
        conn.send(b'Thanks')
    conn.close()


if __name__ == '__main__':
    main("127.0.0.1", 8001)
