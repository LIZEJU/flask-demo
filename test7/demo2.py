# -*- coding:utf-8 -*-
# Author: 李泽军
# Date: 2019/12/13 1:09 PM
# Project: test

from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy import  Column , Integer , String

# 创建声明基类
Base = declarative_base()


# 创建user类
class User(Base):

    __tablename__ = 'user' # 指定数据表明
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    email = Column(String(50))

    def __repr__(self):
        return  '<user<name=%s>'%self.name

# 创建user类
class Course(Base):

    __tablename__ = 'course' # 指定数据表明
    id = Column(Integer,primary_key=True)
    name = Column(String(50))


    def __repr__(self):
        return  '<user<name=%s>'%self.name
'''
__repr__ 会在直接调用实例对象的时候被调用
'''

print(User.__table__)



if __name__ == '__main__':
    Base.metadata.create