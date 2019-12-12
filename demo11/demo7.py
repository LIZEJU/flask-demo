#encoding:utf-8

import requests

# 设置需要发送的数据
user_info = {'name': 'shixiaolou', 'password': 'abc123', 'hobbies': ['code', 'swim']}
# 向 URL 发送 post 请求
r = requests.post("http://127.0.0.1:5000/register", data=user_info)
# 打印返回文本
print(r.text)