#encoding:utf-8

import  os
from multiprocessing import  Process

def hello(name):
    print('child process:{}'.format(os.getpid()))
    print('hello '+name)

def main():
    print('parent process:{}'.format(os.getpid()))

    p = Process(target=hello,args=('shiyanlou',))
    print('child process start')

    p.start()
    p.join()
    # 子进程完成以后，继续完成主进程
    print('child process stop')
    print('parent process:{}'.format(os.getpid()))

if __name__ == '__main__':
    main()