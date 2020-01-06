'''
常用统计
'''
import  numpy as np
from pandas import DataFrame

df1 = DataFrame(np.arange(9).reshape(3,3), columns=list('ABC'), index=list('abc'))
print(df1)
'''
   A  B  C
a  0  1  2
b  3  4  5
c  6  7  8
'''
print(df1.sum()) # 默认统计每列的和
'''
A     9
B    12
C    15
'''
print(df1.sum(axis=1)) # axis=1 统计每行的和
'''
a     3
b    12
c    21
'''

print(df1.mean()) # 统计每列的平均值
'''
A    3.0
B    4.0
C    5.0
'''

print(df1.describe()) # 获得当前数据的一些统计信息
'''
         A    B    C
count  3.0  3.0  3.0
mean   3.0  4.0  5.0
std    3.0  3.0  3.0
min    0.0  1.0  2.0
25%    1.5  2.5  3.5
50%    3.0  4.0  5.0
75%    4.5  5.5  6.5
max    6.0  7.0  8.0
- `count` 元素值的数量；
- `mean` 平均值；
- `std` 标准差；
- `min` 最小值；
- `25%` 下四分位数；
- `50%` 中位数；
- `75%` 上四分位数；
- `max` 最大值；
'''
