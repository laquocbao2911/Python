import numpy as np
from matplotlib import pyplot as plt
def solve(A,b):
    return np.linalg.solve(A.T@A,A.T@b)
A = np.array([[2000,1],[6000,1],[20000,1],[30000,1],[40000,1]])

b = np.array([[20],[18],[10],[6],[2]])

data = np.array([[2000, 20],
                 [6000, 18],
                 [20000, 10],
                 [30000, 6],
                 [40000, 1]])

x, y = data.T
plt.scatter(x,y)
x1,y1= np.linalg.solve(A.T@A,A.T@b)
plt.scatter(x1,y1,color='brown')
plt.show()