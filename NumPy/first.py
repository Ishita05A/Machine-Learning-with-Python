import numpy as np
a = np.array([1, 2, 3])
print(a)
b = np.array([[1, 2, 3, 5], [3, 4, 5, 6]])
print(b)
print(a.ndim)  # dimension
print(b.ndim)
print(a.shape)
print(b.shape)  # (row,columns)
print(a.dtype)
print(a.itemsize)
print(a.nbytes)  # How many bytes each elements take
print(b.itemsize)  # Total memory consumed by array
print(b.nbytes)
