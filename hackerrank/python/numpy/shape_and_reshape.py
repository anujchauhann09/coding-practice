import numpy as np 

arr_list = input().strip().split(' ')

arr = np.array(arr_list, int)
arr.shape = (3,3)

print(arr)