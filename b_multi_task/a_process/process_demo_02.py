"""
    进程内存案例
"""
from multiprocessing import Process
from time import sleep

a = 1  # 全局变量


def func():
    print("process running...")
    sleep(3)
    print("process end...")

    global a
    print("sub process a:", a)  # sub process a: 1

    # 只修改子进程内存, 与父进程无关
    a = 10000


ps = Process(target=func)

ps.start()

print("main running...")
sleep(4)
print("main end...")

"""
    p.join([timeout])
    功能: 阻塞等待子进程退出
    参数: 最长等待时间
"""
ps.join()  # 阻塞等待子进程结束
print("main a:", a)  # main a: 1
