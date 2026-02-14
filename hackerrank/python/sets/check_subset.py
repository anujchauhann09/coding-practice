T = int(input())

for _ in range(T):
    nA = int(input())
    A = set(map(int, input().split()))
    
    nB = int(input())
    B = set(map(int, input().split()))
    
    is_subset = True
    
    for element in A:
        if element not in B:
            is_subset = False
            break
    
    print(is_subset)
