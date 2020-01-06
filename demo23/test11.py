import  numpy as np
import  matplotlib.pyplot as plt
from pandas import Series ,DataFrame
import  pandas as pd

s = Series(np.random.randn(10).cumsum(),index=np.arange(0,100,10))

print(s.plot()) #AxesSubplot(0.125,0.11;0.775x0.77)
plt.savefig('10.png')
plt.show()

df = DataFrame(np.random.rand(5,4),columns=['A', 'B', 'C', 'D'])
print(df.boxplot())
plt.savefig('11.png')
plt.show()