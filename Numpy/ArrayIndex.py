import numpy as np

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
row_r1 = a[1, :]
# Lấy ra
row_r2 = a[1:2, :] # Lấy ra
print(a.shape)
print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)