import pandas as pd

import  numpy as np

from pandas import Series, DataFrame

s1 = Series([1,2,3,4,5])
print(s1)
# 设置索引名称
s2 = Series([1,2,3,4,5],index=['a', 'b', 'c', 'd', 'e'])
print(s2)
#返回值为指定维度的array np.random.randn(4,4)   shape (4,4)
a3 = np.arange(16).reshape(4,4)
df = DataFrame(a3+1, index=['a', 'b', 'c', 'd'], columns=['A', 'B', 'C', 'D'])
print(df)
a3 =  np.random.randn(4,4)
print(a3)
print(a3.shape)
print(df.index)
print(df.columns)