import  numpy as np
import  matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1,1,1) # 定义在画布的位置1，1，1 占有整个画布

# 设置标题
ax.set_title('axes example')

major_ticks = np.arange(0,101,20)
manjor_ticks = np.arange(0,101,5)

# 设置刻度
ax.set_xticks(major_ticks)
ax.set_xticks(manjor_ticks,minor=True)
ax.set_yticks(major_ticks)
ax.set_yticks(manjor_ticks,minor=True)

# 设置x ,y 轴标签
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')

# 设置网格
ax.grid(which='minor',alpha=0.2)
ax.grid(which='major',alpha=0.5)
# 添加文字
ax.text(42.5,50,'hello')
plt.savefig('4.png')
plt.show()


