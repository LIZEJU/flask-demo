'''
常用运算
'''
import  numpy as np
from pandas import  Series,DataFrame

df1 = DataFrame(np.arange(9).reshape(3,3), columns=list('ABC'), index=list('abc'))
print(df1)
'''
   A  B  C
a  0  1  2
b  3  4  5
c  6  7  8
'''
f = lambda x: x.max() - x.min()

c = df1.apply(f)
print(c)
'''
A    6
B    6
C    6
'''
print(df1.max()) # 每一列的最大值
'''
A    6
B    7
C    8
'''
print(df1.min()) # 每一列的最小值
'''
A    0
B    1
C    2
'''

print(df1.apply(f,axis=1)) # 每一行的最大值和最小值之差
'''
a    2
b    2
c    2
'''
print(df1.apply(f,axis=0)) # 每一列的最大值和最小值之差，默认每一列
'''
A    6
B    6
C    6
以上代码中，我们定义了 f 匿名函数，该匿名函数简单的返回列表的极差，
然后首先通过 df.apply(f) 应用 f, 统计出了每列的极差，接着通过传入 
axis=1 参数，统计出了每行的极差，
如果想将某函数应用到每一个元素上，对于 DataFrame 数据可使用 df.applymap 
方法，而对于 Series 数据可以使用 s.map 方法：
'''

print(df1.applymap(lambda x:x+1)) # 应用到每一个元素
'''
   A  B  C
a  1  2  3
b  4  5  6
c  7  8  9
'''
# git config remote.origin.url 'git://github.com/LIZEJU/flask-demo.git'

print(df1.apply(lambda x:x+1))