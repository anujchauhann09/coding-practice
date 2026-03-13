t = int(input())

for _ in range(t):
    s = input().strip()
    
    if s.count('.') != 1:
        print(False)
        continue
    
    if s[0] in "+-":
        s = s[1:]
    
    left, right = s.split('.')
    
    if right.isdigit() and (left == "" or left.isdigit()):
        print(True)
    else:
        print(False)