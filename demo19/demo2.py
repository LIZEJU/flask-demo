import numpy as np

a1 = np.arange(12)

print(a1[:2])
print(a1[2:4])
print(a1[1:5:2])
print(a1[1:10:2])

a1[1:5] = -1
print(a1)

a2 = a1.reshape((3,4))
print(a2.shape)
print(a2.ndim)
print(a2.size)
print(a2)

print(a2[0])
print(a2[1])
print(a2[:,0])
print(a2[:,1])
print(a2[:,2])
print(a2[0,0])
print(a2[0,1])
print(a2[1,1])
