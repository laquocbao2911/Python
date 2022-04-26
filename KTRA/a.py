import numpy as np
A = np.array ([[1 ,-4, 2, 1],[0,2,-3, 1]])
A1 = np.where(A<0, 1000 , A)
print(A1)