import numpy as np

n, m = map(int, input().split())
arr_list = []

for _ in range(n):
    row = list(map(int, input().split()))
    arr_list.append(row)
        
arr = np.array(arr_list)

print(np.transpose(arr))
print(arr.flatten())