'''
缺失值和数据自动对齐
'''

import  numpy as np
from pandas import  Series,DataFrame

s1 = Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s1)

s2 = Series([2, 3, 4, 5], index=['b', 'c', 'd', 'e'])
print(s2)

print(s1+s2)
'''
a    NaN
b    4.0
c    6.0
d    8.0
e    NaN
，相同索引上的值会相加，但不重叠的索引引入 NaN 值，
也就是缺失值。而缺失值会在运算中传播，所以最终结果也是 NaN 值。
根据相同的索引进行自动计算，这就是自动对齐功能
'''

df1 = DataFrame(np.arange(9).reshape(3,3), columns=list('ABC'), index=list('abc'))
print(df1)

df2 = DataFrame(np.arange(12).reshape(3,4), columns=list('ABDE'), index=list('bcd'))
print(df2)

print(df1 + df2)

'''
DataFrame 的计算也会进行自动对齐操作，这个时候没有的行或者列会使用 NaN 值自动填充，
而由于 NaN 值会传播，所以相加的结果也是 NaN。当然我们在计算时，可以指定使用值来填充
 NaN 值
'''
df3 = df1.add(df2,fill_value=0)
print(df3)