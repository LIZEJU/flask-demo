#encoding:utf-8



import re
from datetime import datetime
from collections import  Counter

# 使用正则表达式解析日志文件，返回数据列表
def open_parser(filename):
    with open(filename) as logfile:
        # 使用正则表达式解析日志文件
        pattern = (r''
                   r'(\d+.\d+.\d+.\d+)\s-\s-\s'  # IP 地址
                   r'\[(.+)\]\s'  # 时间
                   r'"GET\s(.+)\s\w+/.+"\s'  # 请求路径
                   r'(\d+)\s'  # 状态码
                   r'(\d+)\s'  # 数据大小
                   r'"(.+)"\s'  # 请求头
                   r'"(.+)"'  # 客户端信息
                   )
        parsers = re.findall(pattern, logfile.read())
    return parsers

def logs_count():

    # 使用正则表达式解析日志文件
    logs = open_parser('nginx.log')

    '''
    1. 解析文件就是分离不同类型数据（IP，时间，状态码等）
    2. 从解析后的文件中统计挑战需要的信息
    '''
    ip_list = []
    request404_list = []

    for log in logs:

        dt = datetime.strptime(log[1][:-6],"%d/%b/%Y:%H:%M:%S")
        # print(dt)

        if int(dt.strftime("%d")) == 11:
            ip_list.append(log[0])
        if int(log[3]) == 404:
            request404_list.append(log[2])

    # print(ip_list)
    # print(request404_list)
    return ip_list, request404_list

def main():
    ip_list , request404_list = logs_count()
    ip_counts = Counter(ip_list)
    request404_counts = Counter(request404_list)

    # print(ip_counts)
    # print(request404_counts)
    # 将字典按values 排序
    sorted_ip = sorted(ip_counts.items(),key=lambda x:x[1])
    sorted_request404 = sorted(request404_counts.items(),key=lambda x:x[1])
    # print(sorted_ip)

    # 获得最多的一条记录
    # ip_dict = dict([sorted_ip[:5:-1]])
    # url_dict = dict([sorted_request404[:5:-1]])
    # ip_dict = []
    # for i in sorted_ip:
    #     ip_dict.append(dict([i]))
    # print(ip_dict)
    ip_dict = list(map(lambda x:dict([x]),sorted_ip))
    print(ip_dict)
    url_dict = list(map(lambda x:dict([x]),sorted_request404))
    print(url_dict)
    # return  ip_dict,url_dict

if __name__ == '__main__':
    # ip_dict, url_dict = main()
    # print(ip_dict)
    # print(url_dict)
    main()

