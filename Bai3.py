import numpy as np
def solve(A,b):
    return np.linalg.solve(A.T@A,A.T@b)
# a
A=np.array([[0,1],[1,1],[2,1],[3,1]])
b=np.array([[0],[1],[2],[3]])
print(solve(A,b))
# b
A=np.array([[1,1],[2,1],[4,1],[5,1]])
b=np.array([[0],[1],[2],[3]])
print(solve(A,b))
# c
A=np.array([[-1,1],[0,1],[1,1],[2,1]])
b=np.array([[0],[1],[2],[3]])
print(solve(A,b))
# d
A=np.array([[2,1],[3,1],[5,1],[6,1]])
b=np.array([[0],[1],[2],[3]])
print(solve(A,b))