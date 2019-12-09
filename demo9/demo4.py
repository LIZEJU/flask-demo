#encoding:utf-8

'''
处理nginx日志
wget http://labfile.oss.aliyuncs.com/courses/1013/week3/nginx.log


'''


import re
from datetime import datetime

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

def main():

    # 使用正则表达式解析日志文件
    logs = open_parser('nginx.log')

    '''
    1. 解析文件就是分离不同类型数据（IP，时间，状态码等）
    2. 从解析后的文件中统计挑战需要的信息
    '''
    # print(logs)
    ip_dict = {}
    url_dict = {}
    count = 1
    for i in logs:
        if i[0] in ip_dict.keys():
            ip_dict[i[0]] += 1
        else:
            ip_dict[i[0]] =1
    # print(ip_dict)

    for i in logs:
        if i[3] == '404':
            if i[2] in url_dict.keys():
                url_dict[i[2]] += 1
            else:
                url_dict[i[2]] = 1
    url_dict.pop('/robots.txt')
    # print(url_dict)


    return ip_dict, url_dict


if __name__ == '__main__':
    ip_dict, url_dict = main()
    print(ip_dict)
    print(url_dict)
    # main()
