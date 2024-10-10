"""
    GUI问题测试
"""
import time
from threading import Thread


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


result = 0


def prime_sum(begin, end):
    res = []
    for i in range(begin, end):
        if is_prime(i):
            res.append(i)
    global result
    result += sum(res)


def thread_4():
    jobs = []
    for i in range(1, 100001, 25000):
        t = Thread(target=prime_sum, args=(i, i + 25000))
        jobs.append(t)
        t.start()

    for i in jobs:
        i.join()
    print(result)


start_time = time.time()
thread_4()
end_time = time.time()
print("using time:", end_time - start_time)
