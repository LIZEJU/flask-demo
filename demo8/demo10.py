#encoding:utf-8

import  base64

data = base64.b64encode(b'hello pyt')
print(data)

d1 = base64.b64decode(data)
print(d1)

from configparser import  ConfigParser

config = ConfigParser()

d1 = config.read('syl.ini',encoding='utf8')
print(d1)

sections = config.sections()
print('sections:{}'.format(sections))

user = config.options('user')
print('user:{}'.format(user))
user_info = config.items('user')
print('user_info:{}'.format(user_info))
user_name = config.get('user','name')
print('user_name:{}'.format(user_name))

config.add_section('pwd')
config.set('pwd','password','1234')
with open('syl.ini','w',encoding='utf8') as f:
    config.write(f)

