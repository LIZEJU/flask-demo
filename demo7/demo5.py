#encoding:utf-8

'''
生成器
'''

# 使用生成器表达式创建一个生成器并迭代
g = (x*x for x in range(1,4))
print(g)

for x in g:
    print(x)

def fib(n):
   current = 0
   a, b = 1, 1
   while current < n:
       yield a
       a, b = b, a + b
       current += 1

f5 = fib(5)
print(f5)

for x in f5:
    print(x)