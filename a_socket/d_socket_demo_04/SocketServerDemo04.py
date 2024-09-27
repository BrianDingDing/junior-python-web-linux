from socket import *

SERVER_ADDR = ("0.0.0.0", 8888)
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(SERVER_ADDR)
sock.listen()

print("等待连接...")
conn, addr = sock.accept()
print("连接了", addr)

while True:
    data = conn.recv(1024)
    # 1. 防止客户端异常退出 (not data), 接收客户端退出信号 (b"##" == data)
    if not data or b"##" == data:
        break
    print("收到了:", data.decode())
    conn.send(b"Thanks")

conn.close()
sock.close()
