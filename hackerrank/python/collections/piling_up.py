from collections import deque

T = int(input())

for _ in range(T):
    n = int(input())
    blocks = deque(map(int, input().split()))
    
    last = float('inf')
    possible = True
    
    while blocks:
        if blocks[0] >= blocks[-1]:
            pick = blocks.popleft()
        else:
            pick = blocks.pop()
        
        if pick > last:
            possible = False
            break
        
        last = pick
    
    print("Yes" if possible else "No")