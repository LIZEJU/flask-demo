#encoding:utf-8

import  threading

def hello(name):
    print('当前的子线程：{}'.format(threading.get_ident()))

    print('hello'+name)

def main():
    print('当前主线程：线程id:{}'.format(threading.get_ident()))
    print('----------------')
    t = threading.Thread(target=hello,args=('python',))
    t.start()
    t.join()

    print('----------------')
    print('档期为主线程，线程id:{}'.format(threading.get_ident()))

if __name__ == '__main__':
    main()