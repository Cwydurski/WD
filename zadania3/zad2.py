import numpy as np
m = np.array([[3,4,9], [1,2,3], [8,5,7]])
n = np.array([[3,4,1,2], [1,2,2,4], [8,5,4,9], [4,7,1,2]])
print(m.min(axis=1))
print(m.min(axis=0))
print(n.min(axis=1))
print(n.min(axis=0))