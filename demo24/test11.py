from test9 import courses_ts_W,courses_ts
# 每次做单独分析时，最好复制一份整理好的数据，减少对原数据集影响
courses_ts_A = courses_ts.copy()
# 计算平均学习时间并添加列
courses_ts_A['平均学习时间'] = courses_ts_A['学习时间'] / courses_ts_A['学习人数']
print(courses_ts_A.head())

a = courses_ts_A.sort_values(by='平均学习时间', ascending=False).head()
print(a.head())

b = courses_ts_A.sort_values(by='平均学习时间', ascending=False).tail()
print(b)
count = 0
for i in courses_ts_A['学习时间']:
    if i == 0 :
        i = 0.1

    courses_ts_A['学习时间'][count] = i
    count += 1
courses_ts_A['人均/学习时间'] = courses_ts_A['学习人数'] / courses_ts_A['学习时间']

c = courses_ts_A.sort_values(by='人均/学习时间', ascending=False).head()
print(c)
