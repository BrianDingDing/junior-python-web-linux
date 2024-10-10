"""
    基于多线程的TCP网络并发模型(面向对象)
"""
from socket import socket
from threading import Thread


# 搭建并发网络
class ThreadServer:

    def __init__(self, host='127.0.0.1', port=8000):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.sock = self._create_socket()

    def _create_socket(self):
        sock = socket()
        sock.bind(self.address)
        return sock

    # 这是启动服务方法. 启动服务后, 客户端才能连接.
    def server_forever(self):
        self.sock.listen()
        print("Listen the port %d" % self.port)

        # 循环处理连接
        while True:
            try:
                conn, addr = self.sock.accept()
                print(f"Connect from: {addr}")
            except KeyboardInterrupt:
                self.sock.close()
                break

            # 创建启动线程
            Handler(conn).start()


# 处理客户端请求
class Handler(Thread):

    def __init__(self, conn):
        self.conn = conn
        Thread.__init__(self, daemon=True)

    # 具体处理客户端请求
    def run(self):
        while True:
            data = self.conn.recv(1024)
            if not data or data == b'##':
                break
            print(data.decode())
            self.conn.send(b'Thanks')
        self.conn.close()


if __name__ == '__main__':
    server = ThreadServer(host="127.0.0.1", port=8001)
    server.server_forever()  # 启动网络服务
