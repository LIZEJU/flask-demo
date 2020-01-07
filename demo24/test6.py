import  numpy as np
import  pandas as pd

# 生成时间戳索引
i = pd.date_range('2017-1-1',periods=20,freq='M')
print(i)

# 生成随机数据并添加时间戳作为索引
data = pd.Series(np.random.randn(len(i)),index=i)
print(data)

# 检索2017的所有数据
print(data['2017'])

# 检索2017，7月到3月之间的所有的数据
print(data['2017-07':'2018-03'])

# 使用loc方法检索2017年1月的所有的数据
print(data.loc['2017-01'])
print(data.loc['2017-12':'2018-04'])
# 使用truncate方法检索2017-3-1 到2018-4-2期间的数据
print(data.truncate(before='2017-3-1',after='2018-4-2'))
