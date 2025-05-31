import numpy as np
before = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])
print(before)
print(before.shape)
after = before.reshape([1, 8])
print(after)
