import numpy as np

n, m = map(int, input().split())
arr = []

for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
    
arr = np.array(arr)
mini_values = np.min(arr, axis = 1)

print(np.max(mini_values))