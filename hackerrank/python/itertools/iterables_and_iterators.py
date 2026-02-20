from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

total = list(combinations(range(n), k))

count = 0

for comb in total:
    if any(letters[i] == 'a' for i in comb):
        count += 1

print(round(count / len(total), 4))