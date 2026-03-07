n, m = map(int, input().split())

table = []
for _ in range(n):
    table.append(list(map(int, input().split())))

k = int(input())

table.sort(key=lambda row: row[k])

for row in table:
    print(*row)