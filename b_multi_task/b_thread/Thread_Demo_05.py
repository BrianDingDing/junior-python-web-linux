from time import sleep
from threading import Thread, Lock

tickets = ["T%d" % item for item in range(1, 501)]

lock = Lock()


def sell(w):
    while tickets:
        sleep(0.01)
        # 解决票重复问题
        lock.acquire()
        # 多一个判断，防止已经没有票了还删除
        if tickets:
            print("%s -- %s" % (w, tickets[0]))
            del tickets[0]
        lock.release()


jobs = []
for i in range(1, 11):
    t = Thread(target=sell, args=("W%d" % i,))
    jobs.append(t)
    t.start()

for item in jobs:
    item.join()

print("all has been sold...")
