# -*- coding:utf-8 -*-
# Author: 李泽军
# Date: 2019/12/13 2:38 PM
# Project: test

'''
简单的crud操作
'''

from test7.demo5 import  engine
from sqlalchemy.orm.session import sessionmaker
from test7.demo4 import  Courses ,User , Lab
from test7.demo2 import Course
Session = sessionmaker(bind=engine)
session = Session()

data = session.query(Courses).first()
print(data)

data1 = session.query(Course).first()
print(data1)

# user = User(name='pwd',email='pwd@qq.com')

# session.add(user)
# session.commit()
print('添加用户')
user = session.query(User).first()

# courses = Courses(name='java',teacher_id=user.id)
# session.add(courses)
# session.commit()

print('添加课程')
print('查看课程')
courses = session.query(Courses).first()
print(courses)

# lab1 = Lab(name='orm基础',course_id=courses.id)
# lab2 = Lab(name='关系数据库',course_id=courses.id)
# session.add(lab1)
# session.add(lab2)
# session.commit()
print('查看lab')
# data1 = session.query(Lab).first()
# print(data1)
# session.delete(data1)
data = session.query(Lab).all()
for i in data:
    print(i)
# 删除lab
print('删除lab')
lab1 = session.query(Lab).first()
print(lab1.name)
print(lab1.course.name)
session.delete(lab1)
session.commit()

'''
UnicodeEncodeError: 'latin-1' codec can't encode characters in position 3-4: ordinal not in range(256)
解决办法：
charset=utf8
engine = create_engine('mysql://root:1234@localhost:3306/shiyanlou?charset=utf8')
'''