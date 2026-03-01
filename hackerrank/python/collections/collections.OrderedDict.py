from collections import OrderedDict

ordered_items = OrderedDict()
N = int(input())

for _ in range(N):
    *item, price = input().split()
    item = " ".join(item)
    ordered_items[item] = ordered_items.get(item, 0) + int(price)

for item, total in ordered_items.items():
    print(item, total)