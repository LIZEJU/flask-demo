# -*- coding:utf-8 -*-
# Author: 李泽军
# Date: 2019/12/13 1:24 PM
# Project: test

from sqlalchemy.orm import  relationship
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import  declarative_base
from test7.demo1 import  engine
from sqlalchemy import  Column , Integer, String


Base = declarative_base(bind=engine)
# 创建user类
class User(Base):

    __tablename__ = 'user' # 指定数据表明
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    email = Column(String(50))

    def __repr__(self):
        return  '<user<name=%s>'%self.name
class Courses(Base):
    __tablename__ = 'courses'

    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    teacher_id = Column(Integer,ForeignKey('user.id'))
    teacher = relationship("User",backref='user')

    def __repr__(self):
        return 'courses(name=%s)'%self.name


class Lab(Base):
    __tablename__ = 'lab'

    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    course_id = Column(Integer,ForeignKey('courses.id'))
    course = relationship('Courses',backref='labs')

    def __repr__(self):
        return '<lab(name=%s)'%self.name

if __name__ == '__main__':
    Base.metadata.create_all(engine)
