import numpy as np
a = np.ones((3, 3))
b = np.full((3, 2), 2)
print(np.matmul(a, b))
print(np.linalg.det(a))
