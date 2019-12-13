# -*- coding:utf-8 -*-
# Author: 李泽军
# Date: 2019/12/13 2:30 PM
# Project: test


from sqlalchemy.engine import  create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column,String,Integer,Text
from sqlalchemy.orm.session import  sessionmaker


engine = create_engine('mysql://root:1234@localhost:3306/shiyanlou?charset=utf8')

Base = declarative_base(bind=engine)

class Path(Base):
    __tablename__ = 'path'

    id = Column(Integer,primary_key=True)
    name = Column(String(64),nullable=False)
    config = Column(String(128))

# if __name__ == '__main__':
#     # Base.metadata.create_all(engine)
#     data = engine.execute('show tables;').fetchall()
#     for i in data:
#         print('tb:{}'.format(i[0]))
#     data1 = engine.execute('desc path;').fetchall()
#     print(data1)