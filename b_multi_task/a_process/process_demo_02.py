"""
    进程内存案例
"""
from multiprocessing import Process
from time import sleep

a = 1  # 全局变量


def func():
    global a
    print("sub process a:", a)  # sub process a: 1

    # 只修改子进程内存, 与父进程无关
    a = 10000
    print("sub process1 a:", a)  # sub process a: 1

    sleep(1)


ps = Process(target=func)
ps.start()

"""
    p.join([timeout])
    功能: 父进程阻塞并等待子进程退出
    参数: 最长等待时间
"""
ps.join()
print("main a:", a)  # main a: 1
