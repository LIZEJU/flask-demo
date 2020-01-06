import  numpy as np

import matplotlib.pyplot as plt
from PIL import Image

N = 50
x = np.random.randn(N)
y = np.random.randn(N)
colors = np.random.randn(N)

area = np.pi * (15 * np.random.randn(N))**2

plt.scatter(x,y,s=area,c=colors,alpha=0.5)


plt.savefig('2.png')
plt.show()