"""
    假设有500张票, 记作T1-T500 放在一个列表中, 创建10个分支线程, 模拟10个卖票窗口(w1 - w10)，同时卖这500张票
    每卖出张需要打印 “W1 -- T250”, 同时需要sleep(0.1)模拟出票时间
    直到所有票卖完, 所有线程结束, 打印依据"票已售罄".
"""
from time import sleep
from threading import Thread

# 500张票
tickets = ["T%d" % item for item in range(1, 501)]


# 卖票过程
def sell(w):
    while tickets:
        sleep(0.01)
        print("%s -- %s" % (w, tickets.pop(0)))


# 创建线程
jobs = []
for i in range(1, 11):
    t = Thread(target=sell, args=("W%d" % i,))
    jobs.append(t)
    t.start()

# 所有线程结束时打印
for item in jobs:
    item.join()

print("all has been sold...")
