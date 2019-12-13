# -*- coding:utf-8 -*-
# Author: 李泽军
# Date: 2019/12/13 4:15 PM
# Project: test

from test7.demo8 import db ,Title , Category
from datetime import  datetime

cate = Category.query.filter_by(id=1).first()
print(cate.name)

t1  = Title(name='linux',category=cate,content='12313',created_time=datetime.now())
t2  = Title(name='云计算',category=cate,content='12313',created_time=datetime.now())

db.session.add(t1)
db.session.add(t2)
db.session.commit()