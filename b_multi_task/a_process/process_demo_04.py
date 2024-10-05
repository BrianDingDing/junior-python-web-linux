"""
    创建多个子进程
"""

from multiprocessing import Process
import os
from time import sleep


def th(sec, action):
    sleep(sec)
    print(action)
    """
        os.getpid()
        功能: 获取一个进程的PID值
        返回值: 返回当前进程的PID 
    """

    """
        os.getppid()
        功能: 获取父进程的PID号
        返回值: 返回父进程PID
    """
    print(os.getppid(), "---", os.getpid())


jobs = []  # 存储子进程对象
for data in [(4, "eating"), (2, "sleeping"), (3, "fighting")]:
    p = Process(target=th, args=data)
    jobs.append(p)
    p.start()

# 取出所有子进程对象判断是否结束
for item in jobs:
    item.join()

print("ending...")
