n = int(input())
s = set(map(int, input().split()))

m = int(input())

for _ in range(m):
    parts = input().split()
    command = parts[0]

    if command == 'pop':
        if s:
            s.pop()
    elif command == 'remove':
        if int(parts[1]) in s:
            s.remove(int(parts[1]))   
    elif command == 'discard':
        s.discard(int(parts[1])) 

print(sum(s))
