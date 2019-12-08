#encoding:utf-8

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 获取 numbers 中的所有偶数
num_list = [x for x in numbers if x % 2 == 0]
print(num_list)

num_list = [x for x in numbers if x % 2 == 1]
print(num_list)


num_list = [x * x for x in numbers]
print(num_list)

print('==================')

f = filter(lambda x: x%2 == 0, numbers)
print(list(f))

m = map(lambda x: x * x ,numbers)
print(list(m))

print('字典解析')
d = {'a':1,'b':2,'c':3}
c = {k:v*v for k ,v in d.items()}
print(c)