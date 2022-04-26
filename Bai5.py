
import numpy as np
import math
def solve(A,b):
    return np.linalg.solve(A.T@A,A.T@b)
A=np.array([[np.cos(1),np.sin(1)],
            [np.cos(2),np.sin(2)],
            [np.cos(3),np.sin(3)]
])
b=np.array([[7.9],[5.4],[-9]])
print(solve(A,b))