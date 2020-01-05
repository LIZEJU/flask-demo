from pandas import Series , DataFrame
import  numpy as np
s2 = Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s2)

print(s2[0])
print(s2['a'])

print(s2[0:3])
print(s2['a':'c'])

#，一种是以整数索引（这说明整数索引一直默认存在），
# 第二种方式是通过指定的字符索引进行
#其实整数索引和字符索引，分别调用了 s2.iloc 和 s2.loc 索引，
# 其中 iloc 代表整数索引
s3 = s2.iloc[0:3]
print(s3)
print(s3.loc['a':'c'])
#对于 DataFrame 数据来说，由于有行列之分，所以可以有多种
# 选择数据的方式，比如通过索引或者标签来选择，先看看对于标签
# （列）怎么选
df = DataFrame(np.random.randn(4, 4), index=['a', 'b', 'c', 'd'], columns=['A', 'B', 'C', 'D'])
print(df)
#看看对于标签（列）怎么选择
print(df.A)
print(df['A'])
#选择多列怎么操作
print(df[df.columns[0:2]])
#选择 df 的某行
#可以根据 loc 属性来选择某一行，iloc 根据整数索引来选择某一行

print(df.loc['a'])
print(df.loc['a':'b'])
print(df.iloc[0])

#另外一些方法来选择多个列
print(df.loc[:,['B','C','D']])
print(df.loc[['a','d'],['B','D']])
# loc 第一个参数代表的是行，第二个参数代表的是列
print(df.loc[['a'],['A']])
# print(df.loc[['A'],['a']])
print(df.loc['b':'d','A':'C'])
