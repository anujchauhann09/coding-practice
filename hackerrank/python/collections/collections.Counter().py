from collections import Counter

X = int(input())
shoe_sizes = list(map(int, input().split()))
N = int(input())

inventory = Counter(shoe_sizes)
total = 0

for _ in range(N):
    size, price = map(int, input().split())

    if inventory[size] > 0:
        total += price
        inventory[size] -= 1

print(total)