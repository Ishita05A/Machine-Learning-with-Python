import numpy as np
a = np.array([[[1, 2, 3], [3, 1, 5]], [[2, 4, 5], [3, 4, 5]]])
print(a)
print()
print()
print(a[:, 1, :])
print()
print()
print(a[1, 1, 2])  # [row , column , element idx]
print()
print()
print(a[0:, 1, :])
a[:, 1, :] = [[9, 9, 9], [1, 1, 1]]
print()
print(a)
