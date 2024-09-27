"""
    让客户端退出服务端不会退出, 而是能够继续处理下一个客户端的连接请求.
"""
from socket import *

SERVER_ADDR = ("0.0.0.0", 8888)
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(SERVER_ADDR)
sock.listen()

while True:
    print("等待连接...")
    conn, addr = sock.accept()
    print("连接了", addr)

    while True:
        data = conn.recv(1024)
        if not data or b"##" == data:
            break
        print("收到了:", data.decode())
        conn.send(b"Thanks")
    conn.close()
