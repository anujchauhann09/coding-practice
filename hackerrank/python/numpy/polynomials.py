import numpy as np

coeff = list(map(float, input().split()))
x = float(input())

print(np.polyval(coeff, x))