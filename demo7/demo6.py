#encoding:utf-8

from datetime import datetime
def log(func):
    def decorator(*args, **kwargs):
        print('Function ' + func.__name__ + ' has been called at ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return func(*args, **kwargs)
    return decorator

@log
def add(x,y):
    return  x + y

print(add(1,2))
'''
@ 是 Python 提供的语法糖，语法糖指计算机语言中添加的某种语法，
这种语法对语言的功能并没有影响，但是更方便程序员使用
'''
add = log(add)
print(add(1,3))
print(add.__name__)
'''
@log 装饰 add 后，add 其实已经不再是原来的 add 函数了，
它已经变成了log 函数返回的 decorator 函数
'''
from functools import wraps

def log(func):
     @wraps(func)
     def decorator(*args, **kwargs):
         print('Function ' + func.__name__ + ' has been called at ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
         return func(*args, **kwargs)
     return decorator

@log
def add(x,y):
    return  x + y

print(add.__name__)
print(add(1,5))