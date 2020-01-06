'''
数据合并和分组
'''

import  numpy as np
from pandas import Series,DataFrame

df1 = DataFrame(np.random.randn(3, 3))
print(df1)
df2 = DataFrame(np.random.randn(3, 3), index=[5, 6, 7])
print(df2)
import  pandas as pd
df3 = pd.concat([df1,df2]) # df1 和df2 的索引不同，合并之后，所有的数据会组合在一起
print(df3)

df1 = DataFrame({'user_id': [5348, 13], 'course': [12, 45], 'minutes': [9, 36]})
df2 = DataFrame({'course': [12, 45], 'name': ['Linux 基础入门', '数据分析']})
print(df1)
print(df2)
df3 = pd.merge(df1,df2)
print(df3)
'''
   user_id  course  minutes
0     5348      12        9
1       13      45       36
   course        name
0      12  Linux 基础入门
1      45        数据分析
   user_id  course  minutes        name
0     5348      12        9  Linux 基础入门
1       13      45       36        数据分析
'''
print('222222')
df4 = df1[df1['user_id'] == 13 ]['minutes']
print(df4)
print('11111111111')
df = DataFrame({'user_id': [5348, 13, 5348], 'course': [12, 45, 23], 'minutes': [9, 36, 4]})
# print(df)
print(df[df['user_id'] == 5348 ]['minutes'])
'''
0    9
2    4
Name: minutes, dtype: int64
'''

print(df[df['user_id'] == 5348 ]['minutes'].sum())

print(df[['user_id','minutes']])

print(df[['user_id','minutes']].groupby('user_id').sum())
'''
         minutes
user_id         
13            36
5348          13
我先过滤列，只剩下了 user_id 和 minutes 列，然后通过 groupby 方法在 user_id 列上进行分组并求和
'''
