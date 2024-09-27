from socket import *

SERVER_ADDR = ("127.0.0.1", 8888)
sock = socket()
sock.connect(SERVER_ADDR)

while True:
    msg = input(">> ")
    sock.send(msg.encode())
    if "##" == msg:
        break
    data = sock.recv(1024)
    print(data.decode())

sock.close()
