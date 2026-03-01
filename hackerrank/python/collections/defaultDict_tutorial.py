from collections import defaultdict

n, m = map(int, input().split())

groupA = defaultdict(list)

for i in range(1, n + 1):
    word = input()
    groupA[word].append(i)

for _ in range(m):
    word = input()
    
    if word in groupA:
        print(*groupA[word])
    else:
        print(-1)