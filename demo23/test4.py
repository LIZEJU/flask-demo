import  numpy as np
import  matplotlib.pyplot as plt
from PIL import Image
fig1 = plt.figure()

ax1 = fig1.add_subplot(1,1,1)
print(fig1) #Figure(640x480)
print(plt.gcf()) #Figure(640x480)
print(plt.gca()) #AxesSubplot(0.125,0.11;0.775x0.77)
plt.show()

fig2 = plt.figure()

ax2 = fig2.add_subplot(1,1,1)
print(fig2) #Figure(640x480)
print(plt.gcf()) #Figure(640x480)
print(plt.gca()) #AxesSubplot(0.125,0.11;0.775x0.77)

fig = plt.figure()

ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)

ax1.plot(np.random.randn(50).cumsum(),'k--')
_ = ax2.hist(np.random.randn(100),bins=20,color='k')
ax3.scatter(np.arange(30),np.arange(30)+3*np.random.randn(30))


plt.savefig('3.png')
fig.show()


