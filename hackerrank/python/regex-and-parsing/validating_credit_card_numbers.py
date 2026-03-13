import re

n = int(input())

pattern = r'^[456]\d{3}(-?\d{4}){3}$'

for _ in range(n):
    card = input().strip()
    
    if re.match(pattern, card) and not re.search(r'(\d)\1{3}', card.replace('-', '')):
        print("Valid")
    else:
        print("Invalid")