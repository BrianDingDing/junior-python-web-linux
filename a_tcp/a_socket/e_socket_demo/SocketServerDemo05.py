"""
    粘包问题
"""
from socket import *
from time import sleep

SERVER_ADDR = ("0.0.0.0", 8888)
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(SERVER_ADDR)
sock.listen()

print("等待连接...")
conn, addr = sock.accept()
print("连接了", addr)

while True:
    data = conn.recv(5)
    if not data or b"##" == data:
        break
    print("收到了:", data.decode())
    conn.send(b"Thanks")
    sleep(0.1)  # 控制发送速度

conn.close()
sock.close()
