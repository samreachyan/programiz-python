import numpy as np

a = np.array([1,2,3])
print(type(a))
print(a.shape)

print(a[0], a[1], a[2])
a[0]= 5
print(a)

b = np.array([[1,2,3],[4,5,6]])
print(b.shape)
print(b[0, 0], b[0, 1], b[1, 0])

print('\n\n\n')

c = np.ones((1,2))
print("Here is ones fuction")
print(c)

d = np.zeros((2,2))
print("Here is zeros function")
print(d)

e = np.full((2,2), 7)
print("Here is full function")
print(e)

f = np.eye(2)
print('Here is eye function')
print(f)

g = np.random.random((2,2))
print('Here is random function')
print(g)