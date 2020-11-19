import numpy as np

x = np.array([[1,2],[3,4]])
print(x)
print(np.sum(x)) # Tính tổng tất cả phần tử trong array; prints "10"

print(np.sum(x, axis=0)) # Tính tổng phần tử mỗi hàng; prints "[4 6]"

print(np.sum(x, axis=1)) # Tính tổng phần tử mỗi cột; prints "[3 7]"