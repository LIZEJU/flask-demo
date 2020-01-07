import  pandas as pd
from pandas import  offsets

a = pd.date_range('2017-1-1',periods=10,freq='1D1H')
print(a)

b = a + offsets.DateOffset(months=1, days=1, hours=1)
print(b)

c = a + 2 * offsets.Week()
print(c)
