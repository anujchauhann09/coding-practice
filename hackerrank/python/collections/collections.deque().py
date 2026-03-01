# from collections import deque

# N = int(input())
# d = deque()

# for _ in range(N):
#     command = list(map(str, input().split()))
    
#     if command[0] == 'append':
#         d.append(int(command[1]))
#     elif command[0] == 'pop':
#        d.pop() 
#     elif command[0] == 'popleft':
#         d.popleft()
#     elif command[0] == 'appendleft':
#         d.appendleft(int(command[1]))

# for item in d:
#     print(item, end=" ")

from collections import deque

d = deque()

for _ in range(int(input())):
    cmd = input().split()

    if len(cmd) == 2:
        getattr(d, cmd[0])(int(cmd[1]))
    else:
        getattr(d, cmd[0])()

print(*d)