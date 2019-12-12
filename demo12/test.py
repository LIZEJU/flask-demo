#encoding:utf-8

import  os

print(os.walk(__file__))

for i in os.walk(__file__):
    print(i)
