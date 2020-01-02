import  numpy as np

'''
多维数组的基础运算
'''

a1 = np.arange(12).reshape(3,4)
print(a1)

print('----+')
a2 =a1+1
print(a2)
print('------*')
a3 = a1 * 2
print(a3)

a3 = np.arange(4).reshape(2,2)
a4 = np.arange(4,8).reshape(2,2)
print('11111111111111')
print(a3,a4)

print(a4-a3)

print(a3 + a4 )

# 矩阵乘法
print('矩阵乘法')
print(a3.dot(a4))

# axis
print(a3.sum(axis=0))
print(a3.sum(axis=1))
