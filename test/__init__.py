# -*- coding:utf-8 -*-
# Author: 李泽军
# Date: 2020/1/25 6:48 PM
# Project: flask-demo

message = {'username':'jack lee','text':'new user comin , people count:{}'.format(1)}
import json
message = json.dumps(message)
print(type(message))