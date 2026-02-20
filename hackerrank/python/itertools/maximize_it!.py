from itertools import product

K, M = map(int, input().split())

lists = []

for _ in range(K):
    data = list(map(int, input().split()))
    lists.append(data[1:])  
    
max_value = 0

for comb in product(*lists):
    total = sum(x*x for x in comb) % M
    max_value = max(max_value, total)

print(max_value)