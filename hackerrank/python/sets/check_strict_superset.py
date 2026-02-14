A = set(map(int, input().split()))
n = int(input())

is_strict_superset = True

for _ in range(n):
    other = set(map(int, input().split()))
    
    for element in other:
        if element not in A:
            is_strict_superset = False
            break
    
    if len(A) <= len(other):
        is_strict_superset = False
    
    if not is_strict_superset:
        break

print(is_strict_superset)
