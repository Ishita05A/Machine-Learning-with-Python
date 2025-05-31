import numpy as np
stat = np.array([[1, 2, 3], [2, 45, 6]])
print(stat)
print(np.min(stat))
print(np.max(stat))
print(np.sum(stat, axis=0))  # Column wise sum
print(np.sum(stat, axis=1))  # Row wise sum
