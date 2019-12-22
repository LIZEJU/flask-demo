# -*- coding:utf-8 -*-
# Author: 李泽军
# Date: 2019/12/13 3:09 PM
# Project: test

from demo5 import  engine,Path

from sqlalchemy.orm.session import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()



# path1 = Path(name='Python',config={'description':'python path'})
# path2 = Path(name='BigData',config={'description':'BigData path'})

# session.add(path1)
# session.add(path2)
# session.commit()

data1 = session.query(Path).first()
print(data1)
print(type(data1))
# for i in data1:
#     print(i)
# data = engine.execute('select * from path;').fetchall()
# print(data)