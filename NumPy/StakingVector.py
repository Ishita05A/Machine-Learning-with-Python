import numpy as np
v1 = np.array([1, 2, 3, 4])
v2 = np.array([3, 4, 5, 6])
r = np.vstack([v1, v2, v1, v2])  # Vertical Staking
print(r)
a = np.zeros([2, 3])
b = np.ones([2, 2])
c = np.hstack([a, b])  # Horizontal Staking
print(c)
