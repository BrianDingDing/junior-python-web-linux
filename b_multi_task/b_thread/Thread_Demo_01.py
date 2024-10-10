"""
    创建新的线程
"""
import os
from threading import Thread
from time import sleep

a = 1


# 线程函数
def func():
    for i in range(3):
        sleep(2)
        print(os.getpid(), "new thread")

    global a
    a = 10000


"""
    t = Thread()
    功能: 创建线程对象
    参数: target 绑定线程函数
    args 元组 给线程函数位置传参
    kwargs 字典 给线程函数键值传参
    daemon bool值, 主线程推出时该分支线程也推出
"""
# 实例化线程对象
t = Thread(target=func)
# 启动线程
t.start()

for i in range(4):
    sleep(1)
    print(os.getpid(), "main thread")

"""
    t.join([timeout])
    功能: 阻塞等待分支线程退出
    参数: 最长等待时间
"""
t.join()
print("a: ", a)
