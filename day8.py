#intersection of two arrays
arr1= [1,2,3,4]
arr2= [1,2,5,6]
intersection= list(set(arr1) & set(arr2))
print(intersection)

#3 matrix multiplication
import numpy as n
A = n.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = n.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
C = n.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
res = n.dot(A, n.dot(B, C))
print(res)
