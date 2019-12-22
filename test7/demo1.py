# -*- coding:utf-8 -*-
# Author: 李泽军
# Date: 2019/12/13 1:04 PM
# Project: test

# 导入create_engine 创建engine实例
from sqlalchemy import  create_engine

engine = create_engine('mysql://root:1234@localhost:3306/shiyanlou')
# 执行sql语句
data = engine.execute('select * from course').fetchall()

# for id , name in data:
#     print('id:{},name:{}'.format(id,name))
#
#
# data1 = engine.execute('show tables;').fetchall()

# print(data1)