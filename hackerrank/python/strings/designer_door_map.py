n, m = map(int, input().split())

pattern = '.|.'

# top part
for i in range(n//2):
    print((pattern * (2*i + 1)).center(m, '-'))

# middle part
print('WELCOME'.center(m, '-'))

# bottom part
for i in range(n//2 - 1, -1, -1):
    print((pattern * (2*i + 1)).center(m, '-'))
