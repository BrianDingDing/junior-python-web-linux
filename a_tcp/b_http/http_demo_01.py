"""
    获取http request和response
"""
from socket import *

ADDR = ("0.0.0.0", 8002)

sock = socket()
sock.bind(ADDR)
sock.listen()

# while True:
print("等待浏览器连接...")
conn, addr = sock.accept()
print("浏览器地址:", addr)

# 来自浏览器的HTTP请求
request = conn.recv(1024)
print(request.decode())

# 组织发送http响应
response = "HTTP/1.1 200 OK\r\n"
response += "Content-Type:text/html\r\n"
response += "\r\n"
response += "hello world"
conn.send(response.encode())
