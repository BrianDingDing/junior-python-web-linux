"""
    带有参数的线程函数
"""

from threading import Thread
from time import sleep


def func(name, sec):
    print(f"{name} thread begin...")
    sleep(sec)
    print(f"{name} thread end...")


for i in range(1, 6):
    # args参数写个逗号, 表示元组.
    t = Thread(target=func, args=("T-%d" % i,), kwargs={'sec': 2})
    t.start()
