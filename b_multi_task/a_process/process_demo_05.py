"""
    使用类对要实现的功能进行封装
    通过类实例化对象, 完成功能的时候, 独立的进程执行.
"""
from multiprocessing import Process
from time import sleep


# 自定义进程类
class Music(Process):
    def __init__(self, name):
        Process.__init__(self)  # 重新加载父亲实例变量
        self.name = name

    # 完成具体的进程要做的事情
    def run(self):
        for i in range(3):
            sleep(2)
            print('play:', self.name)


if __name__ == '__main__':
    music = Music("lalala")
    music.start()  # 调用run方法, 作为独立的进程内容执行
