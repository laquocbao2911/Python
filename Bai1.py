import numpy as np
import math
A = np.array([[2,2],[2,3]])
b = np.array([[4],[6]])
print(np.linalg.solve((A.T).dot(A),(A.T).dot(b)))
