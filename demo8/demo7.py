#encoding:utf-8

import time
from multiprocessing import Process, Value, Lock

def func(val, lock):
    for i in range(50):
        time.sleep(0.01)
        # with lock 语句是对下面语句的简写：
        '''
        lock.acquire()
        val.value += 1
        lock.release()
        '''
        # 为 val 变量加锁，结果就是任何时刻只有一个进程可以获得 lock 锁
        # 自然 val 的值就不会同时被多个进程改变
        with lock:
            val.value += 1

def main():
    val = Value('i', 0)
    # 初始化锁
    # Lock 和 Value 一样，是一个函数或者叫方法，Lock 的返回值就是一把全局锁
    # 注意这把全局锁的使用范围就是当前主进程及其子进程，也就是在运行当前这个 Python 文件过程中有效
    lock = Lock()
    processes = [Process(target=func, args=(val, lock)) for i in range(10)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(val.value)

if __name__ == '__main__':
    for i in range(5):
        main()