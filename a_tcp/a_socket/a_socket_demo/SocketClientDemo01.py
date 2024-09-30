"""
    tcp客户端(client)标准流程
"""
from socket import *

# 访问服务端需要的地址
SERVER_ADDR = ("127.0.0.1", 8888)

# 1. 创建tcp套接字
sock = socket()

"""
    sock.connect(server_addr)
    功能: 连接服务器
    参数: 地址元组, 访问服务器使用的地址
"""
# 2. 发起连接
sock.connect(SERVER_ADDR)

# 3. 发送接收内容
msg = input(">> ")
sock.send(msg.encode())  # str -> bytes
data = sock.recv(1024)
print(data.decode())

# 4. 关闭套接字
sock.close()
