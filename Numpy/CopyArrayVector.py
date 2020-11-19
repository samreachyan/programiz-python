import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
v = np.array([9,10])
w = np.array([11, 12])

# Nhân ma trận, output số 219
print(v.dot(w))
print(np.dot(v, w))
# [ax, ay] * [bx, by] = ax * bx + ay * by
print(x.dot(y))
# .dot it's multi and plus
