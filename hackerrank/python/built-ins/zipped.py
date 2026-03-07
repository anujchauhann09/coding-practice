n, m = map(int, input().split())

marks = []
for _ in range(m):   
    marks.append(list(map(float, input().split())))

for student in zip(*marks):   
    print(sum(student) / len(student))