#encoding:utf-8

import  time
from multiprocessing import Process,Value,Lock
import  os

def func(val,lock):
    print('子进程是：{}'.format(os.getpid()))
    for i in range(50):
        time.sleep(0.1)

        with lock:
            val.value += 1



def main():
    val = Value('i',0)
    print(val)
    lock = Lock()
    processs = [Process(target=func,args=(val,lock,)) for i in range(10)]
    print(processs)
    for p in processs:
        p.start()
    for p in processs:
        p.join()

    print(val.value)

if __name__ == '__main__':
    for i in range(5):
        main()