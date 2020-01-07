import  pandas as pd

p1 = pd.to_datetime(['2017-1-1','2018-1-1'])
print(p1)

p2 = pd.to_datetime(['Jul 1,2017','2017-10-10',None])
print(p2)

p3 = pd.to_datetime(['2017/10/1','2017.1.31'])
print(p3)

p4 = pd.to_datetime('1-10-2017')
print(p4)

p5 = pd.to_datetime('1-10-2019',dayfirst=True)
print(p5)

p6 = pd.to_datetime(pd.Series(['2017-1-1','2017-10-1','2018-1-1']))
print(p6)

p7 = pd.to_datetime(pd.DataFrame({'year':[2017,2018,2019],'month':[10,1,12],'day':[12,24,31],'hour':[5,6,7]}))
print(p7)

# # 遇到无效数据，报错
# p8 = pd.to_datetime(['2017-1-1', 'invalid'], errors='raise')
# print(p8)

# 遇到无效数据，忽略
p8 = pd.to_datetime(['2017-1-1', 'invalid'], errors='ignore')
print(p8)

p9 = pd.date_range('2017-1-1','2017-1-3',freq='H')
print(p9)