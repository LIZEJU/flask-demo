#encoding:utf-8

'''
进程间通信
'''

from multiprocessing import Pipe ,Process

# 创建一个管道，注意 Pipe 的实例是一个元组，里面有两个连接器，可以把它们想象成通讯员
conn1 ,conn2 = Pipe()


def send():
    data = 'hello python'
    conn1.send(data)
    print('send data:{}'.format(data))

def recv():
    data = conn2.recv()
    print('recv data:{}'.format(data))

def main():
    Process(target=send).start()
    Process(target=recv).start()

if __name__ == '__main__':
    main()