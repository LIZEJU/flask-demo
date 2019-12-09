#encoding:utf-8

import  os , time , random
from multiprocessing import  Pool


def task(name):
    print('任务{}启动运行：进程id：{}'.format(name,os.getpid()))
    start_time = time.time()

    time.sleep(random.random() * 3 )
    end = time.time()

    print('任务{}结束运行，耗时：{}'.format(name,end-start_time))

if __name__ == '__main__':
    print('当前是主进程，进程id:{}'.format(os.getpid()))
    print('---------------------')

    p = Pool(4)
    for i in range(10):
        p.apply_async(task,args=(i,))
    p.close()
    print('开始运行子进程')
    p.join()
    print('---------------------')
    print('所有子进程运行完毕')
