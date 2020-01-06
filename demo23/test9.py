import  matplotlib.pyplot as plt
import  numpy as np

x = [np.random.randint(0,20) for i in range(10)]
print(x)

y = [np.random.randint(0,20) for i in range(10)]
# x,y 用来设置封闭区域的定点的有序数对，参数color用来完成封闭区域的填充颜色的设置工作
plt.fill(x,y,color='cornflowerblue')
# 完成多边形相对位置的调整
plt.xlim(-1,16)
plt.ylim(-1,16)
# 设置刻度
plt.xticks(np.arange(0,16,5))
plt.yticks(np.arange(0,16,5))
# 保存生成的图片
plt.savefig('8.png')
# 展示绘制效果
plt.show()