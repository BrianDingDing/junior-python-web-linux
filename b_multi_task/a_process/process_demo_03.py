"""
    带有参数的进程函数
"""

from multiprocessing import Process
from time import sleep


def func(name, sec):
    for i in range(3):
        sleep(sec)
        print(f"{name} end process")


"""
    Process()
    功能: 创建进程对象
    参数: target 绑定要执行的目标函数 
          args 元组, 用于给target函数位置传参
          kwargs 字典, 给target函数键值传参
          daemon bool值, 让子进程随父进程退出
"""
# 位置传参
# ps = Process(target=func, args=("Tom", 2))
# ps.start()

# 关键字传参
# ps = Process(target=func, kwargs={"name": "Jerry", "sec": 3})
# ps.start()

# daemon = True
ps = Process(target=func, args=("Tom", 2), daemon=True)
ps.start()
