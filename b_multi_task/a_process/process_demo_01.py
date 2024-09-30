"""
    进程基础创建
"""
from multiprocessing import Process
from time import sleep


# 1. 创建一个进程要执行的函数
def func():
    print("process running...")
    sleep(3)
    print("process end...")


# 2. 实例化进程对象
ps = Process(target=func)

# 3. 启动进程 -> 执行func
ps.start()

print("main running...")
sleep(4)
print("main end...")
