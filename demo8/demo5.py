#encoding:utf-8


from multiprocessing import  Process, Queue


queue = Queue()


def f1(q):
    i = 'helllo pyton'
    q.put(i)
    print('send data:{}'.format(i))

def f2(q):
    data = q.get()
    print('recv data:{}'.format(data))

if __name__ == '__main__':
    Process(target=f1,args=(queue,)).start()
    Process(target=f2,args=(queue,)).start()