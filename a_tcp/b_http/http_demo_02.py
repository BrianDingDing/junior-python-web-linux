"""
    综合案例:
    功能一: 写一个简单的表单(index.html), 包含用户名, 密码和提交按钮. 当浏览器访问服务端时, 将页面返回提供给浏览器.
    功能二: 在前端得到index.html页面后, 输入用户名和密码, 将该用户名和密码存到数据库中.
"""
from socket import *

ADDR = ("0.0.0.0", 8000)


def do_get(conn):
    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Type:text/html\r\n"
    response += "\r\n"
    with open("index.html", "r", encoding="utf8") as fr:
        response += fr.read()
    conn.send(response.encode())


def handler_http(conn):
    request = conn.recv(1024).decode()
    mehtod = request.split(" ")[0]
    if mehtod == "GET":
        do_get(conn)
    elif mehtod == "POST":
        request.split("\n")[-1]


def main():
    sock = socket()
    sock.bind(ADDR)
    sock.listen()

    while True:
        print("等待浏览器连接...")
        conn, addr = sock.accept()
        handler_http(conn)
        print("浏览器地址:", addr)

if __name__ == '__main__':
    main()
