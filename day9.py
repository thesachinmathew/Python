#sum of diagonal, coloumns, rows of a matrix
import numpy as np
m = np.array([
    [2, 5, 8],
    [1, 7, 3],
    [4, 6, 9]
])
rs = m.sum(axis=1)
cs = m.sum(axis=0)
ds = np.trace(m)
ads = np.fliplr(m).trace()
print("Matrix:")
print(m)
print("\nSum of each row:")
print(rs)
print("\nSum of each column:")
print(cs)
print("\nSum of the main diagonal:")
print(ds)
print("\nSum of the anti-diagonal:")
print(ads)
 
