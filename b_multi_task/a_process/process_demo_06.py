import time
from multiprocessing import Process, Queue

"""
    100000以内质数之和, 求得时间, 使用4进程共同执行, 统计使用时间.
"""


# 判断一个数是否为质数
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def prime_sum(num):
    res = []
    for i in range(1, num + 1):
        if is_prime(i):
            res.append(i)
    print(sum(res))


start_time = time.time()
prime_sum(100000)  # 454396537
end_time = time.time()
print("using time:", end_time - start_time)  # 16.57

# """
#     q = Queue(maxsize=0)
#     功能: 创建队列对象
#     参数: 最多存放消息个数
#     返回值: 队列对象
#
#     q.put(data)
#     功能: 向队列存入消息, 满了就阻塞.
#     参数: data 要存入的内容
#
#     q.get()
#     功能: 从队列取出消息, 空了就阻塞.
#     返回值: 返回获取到的内容
#
#     q.full(): 判断队列是否为满
#     q.empty(): 判断队列是否为空
#     q.qsize(): 获取队列中消息个数
# """
# q = Queue()  # 存结果
#
#
# def prime_sum(begin, end):
#     res = []
#     for i in range(begin, end):
#         if is_prime(i):
#             res.append(i)
#     q.put(sum(res))
#
#
# def process_4():
#     for i in range(1, 100001, 25000):
#         p = Process(target=prime_sum, args=(i, i + 25000))
#         p.start()
#
#     res = 0
#     for i in range(4):
#         res += q.get()  # get是阻塞函数, 循环完四次之后, 代表4个进程已经完成
#     print(res)
#
#
# start_time = time.time()
# process_4()  # 454396537
# end_time = time.time()
# print("using time:", end_time - start_time)  # 11.71
