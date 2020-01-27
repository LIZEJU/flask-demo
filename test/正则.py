# -*- coding:utf-8 -*-
# Author: 李泽军
# Date: 2020/1/25 6:48 PM
# Project: flask-demo

import  re
pattern = re.compile('\w+\d+')

s = 'pwdALLLF123'

s1 = pattern.search(s)
if s1:
    print(s1)
    print(s1.group(0))

s2 = '111@#$%'
s3 = pattern.search(s2)
print(s3.group(0))