import numpy as np
import  pandas as pd


# 生成时间戳索引
i = pd.date_range('2017-1-1',periods=5,freq='M')


# 生成随机数据并添加时间戳作为索引
data = pd.Series(np.random.randn(len(i)),index=i)
print(data)

# 将索引向前唯一3个差位，也就是数据向后位移3个单位 , 就是数据从第四个位置开始，前三个位置为空
print(data.shift(3))
# 将索引向后位移3个单位
print(data.shift(-3))

# 将索引的时间向后移动3天
print(data.shift(3,freq='D'))
