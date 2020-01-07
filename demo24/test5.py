import pandas as pd

p1 = pd.Period('2017')
print(p1)

p2 = pd.Period('2017-1')
print(p2)

p3 = pd.Period('2017-1-1')
print(p3)

p4 = pd.Period('2017-1-1 12')
print(p4)

p5 = pd.Period('2017-1-1 12:11')
print(p5)

p6 = pd.Period('2017-1-1 12:05:00')
print(p6)

p7 = pd.period_range('2017-1','2018-1',freq='M')
print(p7)
p8 = pd.Period('2017-1-1')
print(p8)
p9 = pd.Timestamp('2017-1-1')
print(p9)