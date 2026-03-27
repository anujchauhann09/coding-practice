import numpy as np

n, m, p = map(int, input().split())

arr1 = []
arr2 = []

for _ in range(n):
    row = list(map(int, input().split()))
    arr1.append(row)

for _ in range(m):
    row = list(map(int, input().split()))
    arr2.append(row)
    
arr1 = np.array(arr1)
arr2 = np.array(arr2)

print(np.concatenate((arr1, arr2), axis = 0))