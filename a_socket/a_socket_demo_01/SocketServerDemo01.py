"""
    tcp服务端标准流程
"""
from socket import *

# 本机地址
SERVER_ADDR = ("0.0.0.0", 8888)

"""
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    功能: 创建套接字
    参数: family, 网络地址类型, AF_INET表示ipv4(默认值), AF_INET6表示ipv6
          type: 套接字类型, SOCK_STREAM表示tcp套接字(默认值)
    返回值: 套接字对象
"""
# 1. 创建套接字 IPV4     TCP
sock = socket(AF_INET, SOCK_STREAM)

"""
    sock.bind(addr)
    功能: 绑定本机网络地址
    参数: 二元元组(ip, port) e.g ('0.0.0.0', 8888)
"""
# 2. 绑定地址: 让服务端的程序与ip地址绑定, 让客户端找到服务端程序
# 0.0.0.0 表示自动网卡检测ip, 即包含所有地址.
sock.bind(SERVER_ADDR)

"""
    sock.listen()
    功能: 将套接字设置为监听套接字
"""
# 3. 设置监听: 可以被客户端连接, 因为普通客户端的socket是不能被连接的.
sock.listen()

"""
    conn, addr = sock.accept()
    功能: 阻塞等待处理客户端请求
    返回值: conn: 客户端连接套接字; addr: 连接的客户端地址
"""
# 4. 等待并处理客户端连接请求, 函数执行完后三次握手已经执行完.
print("等待连接...")
conn, addr = sock.accept()
print("连接了", addr)

"""
    data = conn.recv(buffersize)
    功能: 接受客户端消息, 也是阻塞函数.
    参数: 每次最多接收消息的大小, 多少字节的数据.
    返回值: 接收到的内容, 收到也是byte格式.

    n = conn.send(data)
    功能: 发送消息
    参数: 要发送的内容, bytes格式.
    返回值: 发送的字节数
"""
# 5. 收发数据
data = conn.recv(1024)
print("收到了:", data.decode())
conn.send(b"Thanks")

# 6. 关闭套接字
conn.close()
sock.close()
