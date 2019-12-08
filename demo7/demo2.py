#encoding:utf-8

t = ('hello','shiyanlou')
a , b = t
print(a)
print(b)

t = ('tom',11)
print('i\'m {}, i\'m {} years old'.format(*t))