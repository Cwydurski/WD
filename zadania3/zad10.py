import numpy as np
b = np.arange(81).reshape(9,9)
print(b)
print(b.shape)
c = b.reshape((3,27))
print(c)