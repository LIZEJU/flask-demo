import  pandas as pd

course_ori = pd.read_table('courses.txt',sep=',',header=0)
# 查看数据的列名称
print(course_ori.columns)
# 预览 DataFrame 前 5 行
print(course_ori.head())

# 课程学习时间变化趋势
i = pd.to_datetime(course_ori['创建时间'])

print(i.head())

courses_ts = pd.DataFrame(data=course_ori.values,columns=course_ori.columns,index=i)
print(course_ori.head())

courses_ts = courses_ts.drop('创建时间',axis=1)
print(courses_ts.head())
# 按照周次频率进行降采样
courses_ts_W = courses_ts.resample('W').sum()
print(courses_ts_W.head())

import matplotlib.pyplot as plt

plt.plot_date(courses_ts_W.index,courses_ts_W['学习时间'], '-')
plt.xlabel('time series')
plt.ylabel('study time')
plt.show()