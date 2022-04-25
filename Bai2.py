import numpy as np
import math

A = np.array([[0,0,1],
              [0,1,1],
              [1,2,1],
              [1,0,1],
              [4,1,1],
              [4,2,1]])
              
b = np.array([[0.5],[1.6],[2.8],[0.8],[5.1],[5.9]])
print(np.linalg.solve((A.T).dot(A),(A.T).dot(b)))