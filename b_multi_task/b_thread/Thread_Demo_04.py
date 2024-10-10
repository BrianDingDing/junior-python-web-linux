"""
    锁演示: 不打印a和b的值
"""

from threading import Thread, Lock
from time import sleep

# 共享资源
a = b = 1

lock = Lock()  # 创建锁对象


# 主线程和分支线程都上锁了, 18行-19行, 28行-30行代码不会同时执行, 一方运行, 一方阻塞. 因此不会打印a和b的值.
def value():
    while True:
        lock.acquire()  # 上锁, 如果lock已经上锁再调用会阻塞
        if a != b:
            print("a = %d,b = %d" % (a, b))
        lock.release()  # 解锁操作


t = Thread(target=value)
t.start()

while True:
    lock.acquire()
    a += 1
    sleep(0.00001)
    b += 1
    lock.release()
