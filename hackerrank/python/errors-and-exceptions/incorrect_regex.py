import re

t = int(raw_input())

for _ in range(t):
    pattern = raw_input()
    try:
        re.compile(pattern)
        print("True")
    except re.error:
        print("False")