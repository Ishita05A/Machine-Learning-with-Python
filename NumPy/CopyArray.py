import numpy as np
a = np.zeros((5, 5))
print(a)
b = np.ones((3, 3))
b[1, 1] = 9
print(b)
a[1:-1, 1:-1] = b
print(a)


x = np.array([1, 2, 3])
y = x
y[0] = 100
print(y)
print(x)  # To avoid this
u = np.array([3, 5, 6])
v = u.copy()
v[1] = 100
print(u)
print(v)
