"""
    死锁过程模拟
"""
from threading import Lock, Thread
from time import sleep


# 银行账户类
class Bank:
    def __init__(self, id, balance, lock):
        self.id = id
        self.balance = balance
        self.lock = lock

    # 取钱
    def get(self, num):
        self.balance -= num

    # 存钱
    def put(self, num):
        self.balance += num


# 转账(死锁)
# def trans(obj1, obj2, num):
#     obj1.lock.acquire()
#     obj1.get(num)  # 减少
#
#     sleep(0.1)
#
#     # 线程1: tom已经上锁同时, 还想给abby上锁, 但此时abby在线程2已经上锁.
#     # 线程2: abby已经上锁同时, 还想给tom上锁, 但此时tom在线程1已经上锁.
#     obj2.lock.acquire()
#     obj2.put(num)  # 增加
#
#     obj1.lock.release()
#     obj2.lock.release()

def trans(obj1, obj2, num):

    # 在上其他锁之前, 先释放自己的锁, 再去锁别人.
    obj1.lock.acquire()
    obj1.get(num)  # 减少
    obj1.lock.release()

    sleep(0.1)

    obj2.lock.acquire()
    obj2.put(num)  # 增加
    obj2.lock.release()


if __name__ == '__main__':
    tom = Bank("10666", 10000, Lock())
    abby = Bank("10668", 4000, Lock())

    t1 = Thread(target=trans, args=(tom, abby, 2000))
    t2 = Thread(target=trans, args=(abby, tom, 2000))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Tom:", tom.balance)
    print("Abby:", abby.balance)
