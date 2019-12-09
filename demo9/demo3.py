#encoding:utf-8

'''

python 端口扫描
端口扫描是一个常见的网络安全用语，它的意思是指客户端向一定范围的服务器端口发送请求，
以此确认端口的开闭状态。端口扫描本身并不是恶意的网络活动，但也是网络攻击者探测目标主机服务，
以利用该服务的已知漏洞的重要手段（维基百科）。在本次挑战中，
'''
import  sys
import  socket

def get_args():
    args = sys.argv[1:]


    print(args)
    host_index = args.index('--host')
    port_index = args.index('--port')
    host_tmp = args[host_index+1]
    port_tmp = args[port_index+1]
    print('host_index :{}'.format(host_index))
    print(host_tmp)
    print('port_index:{}'.format(port_index))
    print(port_tmp)
    if len(host_tmp.split('.')) != 4:
        raise  ValueError
    host = host_tmp

    if '-' in port_tmp:
        port = port_tmp.split('-')
    else:
        port = [port_tmp,port_tmp]
    print('port:{}'.format(port))
    print('host{}:port{}'.format(host,port))

    return  host , [int(port[0]) , int(port[1])]

def scan():

    host , port = get_args()
    print('host:port',host,port)
    open_list = []
    for i in range(port[0],port[1]+1):
        s = socket.socket()
        s.settimeout(0.1)
        print(host,i)
        if s.connect_ex((host,i)) == 0 :
            open_list.append(i)
            print(i,'open')
        else:
            print(i,'closed')
        s.close()
    print(f'completed scan , opening ports at {open_list}')

if __name__ == '__main__':
    scan()
