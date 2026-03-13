import re

n = int(input())

pattern = r'^(?=(?:.*[A-Z]){2})(?=(?:.*\d){3})[A-Za-z0-9]{10}$'

for _ in range(n):
    uid = input().strip()
    
    if re.match(pattern, uid) and len(set(uid)) == 10:
        print("Valid")
    else:
        print("Invalid")