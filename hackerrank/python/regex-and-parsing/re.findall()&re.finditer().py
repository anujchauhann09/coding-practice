import re

s = input()

pattern = r'(?<=[^AEIOUaeiou])([AEIOUaeiou]{2,})(?=[^AEIOUaeiou])'

matches = re.finditer(pattern, s)

found = False

for m in matches:
    print(m.group(1))
    found = True

if not found:
    print(-1)