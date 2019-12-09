#encoding:utf-8

import  time

def io_task():

    time.sleep(1)

def main():
    start_time = time.time()

    for i in range(5):
        io_task()
    end_time = time.time()

    print('程序运行耗时：{}'.format(end_time-start_time))

if __name__ == '__main__':
    main()