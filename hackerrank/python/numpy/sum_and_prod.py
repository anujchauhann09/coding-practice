import numpy as np 

n, m = map(int, input().split())
arr = []

for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
    
arr = np.array(arr)

total_arr = np.sum(arr, axis = 0)
total_prod = np.prod(total_arr)

print(total_prod)
    