import numpy as np

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
b = a[:2, 1:3]

print(a[0, 1])
a[0, 1] = 77
print(a[0, 1])
print(a)
print(b)