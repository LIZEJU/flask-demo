import  numpy as np
# 多维的创建
a1 = np.array([1,2,3,4])
# shape 表示获取多维数组各个维度的大小，返回一个元组
print(a1.shape)

print(a1.size)

print(a1.dtype)

a2 = np.array([1.0,22,3.3])

print(a2.shape)

print(a2.size)

print(a2.dtype)

print(a1)
print(a2)

a3 = np.arange(4)
print(a3)

print(a3.ndim)

a4 = np.ones((4,4),dtype=np.int64)
print(a4)
print(a4.ndim)
print(a4.dtype)
print(a4.shape)

a5 = np.zeros((2,2))
print(a5)
print(a5.shape)
print(a5.ndim)

a6 = np.empty((2,2,))
print(a6)
print(a6.shape)
print(a6.ndim)
print(a6.size)


a7 = np.ones((4,3,4))
print(a7)
print(a7.shape)
print(a7.ndim)
print(a7.size)


a8 = np.arange(12)
print(a8)

a8 = a8.reshape((3,4))
print(a8)

