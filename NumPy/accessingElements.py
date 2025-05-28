import numpy as np
a = np.array([[1, 2, 3, 4, 5, 6], [3, 4, 5, 6, 7, 4]])
print(a[1, 4])
print(a[0, :])
print(a[:, 2])
print(a[0, 1: 5: 2])
a[1, 2] = 45
print(a)
a[:, 3] = [1, 2]
print(a)
