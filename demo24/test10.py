import  matplotlib.pyplot as plt
import  seaborn as sns
from test9 import courses_ts_W,courses_ts
# 新添加一个序数列，方便绘制散点图
courses_ts_W['id'] = range(0,len(courses_ts_W.values))
sns.regplot("id", "学习时间", data=courses_ts_W, scatter_kws={"s": 10}, order=8, ci=None, truncate=True)
plt.xlabel('time series')
plt.ylabel('study time')
# plt.show()
print(courses_ts_W)


sns.regplot("id", "学习人数", data=courses_ts_W, x_bins=10)
plt.xlabel('time series')
plt.ylabel('study time')
# plt.show()
