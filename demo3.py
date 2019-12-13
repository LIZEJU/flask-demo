# -*- coding:utf-8 -*-
# Author: 李泽军
# Date: 2019/12/13 1:15 PM
# Project: test

from sqlalchemy.orm import  sessionmaker
from test7.demo1 import  engine
from test7.demo2 import  User ,Course
Session = sessionmaker(bind=engine)

session = Session()

'''
sessionmaker中有个__call__方法，可以让Session对象可以向函数那样调用
'''

data1 = session.query(Course).all()

print(data1)

data2 = session.query(Course).filter(Course.id==2).first()
print(data2)