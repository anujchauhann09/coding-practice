import re

s = input()
k = input()

pattern = r'(?=(' + k + '))'

matches = list(re.finditer(pattern, s))

if matches:
    for m in matches:
        start = m.start(1)
        end = m.end(1) - 1
        print((start, end))
else:
    print((-1, -1))