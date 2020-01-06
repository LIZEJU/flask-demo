'''
时间序列处理
'''

import  numpy as np
from pandas import Series,DataFrame
from datetime import  datetime ,timedelta

d1 = datetime(2017,8,1)
print(d1)

delta = timedelta(days=10)
print(delta)

d2 = d1 + delta
print(d2)

print('创建时间序列')
dates= [datetime(2018,1,1) , datetime(2018,1,2),datetime(2018,1,3),datetime(2018,1,4)]
print(dates)

ts = Series(np.random.randn(4),index=dates)
print(ts)

print(ts.index)
print(ts.index[0])

print('ts 时间序列')
print(ts.index[0])
print(ts[ts.index[0]])
print(ts['2018-01-01'])
print(ts['2018/01/01'])
print(ts['1/1/2018'])
print(ts[datetime(2018,1,1)])

'''
日期范围：
在 Pandas 中生成日期范围也非常灵活，主要通过 pandas.date_range 函数完成，
该函数主要有以下几个参数:

start: 指定了日期范围的起始时间；
end: 指定了日期范围的结束时间；
periods: 指定了间隔范围，如果只是指定了 
start 和 end 日期的其中一个，则需要改参数；
freq: 指定了日期频率，比如 D 代表每天，H 代表每小时，
M 代表月，这些频率字符前也可以指定一个整数，代表具体多少天，多少小时，
比如 5D 代表 5 天。还有一些其他的频率字符串，比如 MS 代表每月第一天
，BM 代表每月最后一个工作日，或者是频率组合字符串，比如 1h30min 
代表 1 小时 30 分钟。
'''
import  pandas as pd

print(pd.date_range('2018-1-1','2019',freq='M'))
'''
DatetimeIndex(['2018-01-31', '2018-02-28', '2018-03-31', '2018-04-30',
               '2018-05-31', '2018-06-30', '2018-07-31', '2018-08-31',
               '2018-09-30', '2018-10-31', '2018-11-30', '2018-12-31'],
              dtype='datetime64[ns]', freq='M')
'''

print(pd.date_range('2018-1-1','2018-12-1',freq='MS'))
'''
DatetimeIndex(['2018-01-01', '2018-02-01', '2018-03-01', '2018-04-01',
               '2018-05-01', '2018-06-01', '2018-07-01', '2018-08-01',
               '2018-09-01', '2018-10-01', '2018-11-01', '2018-12-01'],
'''


dates = pd.date_range('2017-2-1','2018',freq='MS')
print(dates[-1])
print(dates)
ts = Series(np.arange(len(dates)),index=dates )
print(ts)

print(ts.index)
print(ts.size)
print(ts.head(5))
print(ts.tail(5))


print('ts按每天的数据统计')
print(ts.resample('D').sum())
'''
我们先使用 resample('D') 方法指定了按天统计，接着使用 sum 方
法指定了最终数据是按天的所有数据的和进行统计，当然我们也可以按天
的所有数据的平均数进行统计：
'''

print(ts.resample('D').mean())

print(ts.resample('D').mean().resample('H').mean())
#Pandas 引入了 NaN 值，但当使用 ffill （代表用前面的值替代 NaN 值）就不会有 NaN 值出现:
print(ts.resample('D').mean().resample("D").mean().ffill())

dates = pd.date_range('2020-1-6','2020-1-7',freq='1h30min')
print(dates)