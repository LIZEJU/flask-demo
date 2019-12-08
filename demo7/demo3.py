#encoding:utf-8

# 可迭代对象：使用for循环遍
letters = ['a','b','c']
for i in letters:
    print(i)

# 可迭代对象转为迭代器
it = iter(letters)
it2 = letters.__iter__()

# 迭代器： 使用next函数获取下一个值
print(next(it))
print(next(it2))
print(next(it2))

