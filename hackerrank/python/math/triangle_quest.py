# for i in range(1, int(input())): 
#     for j in range(i, 0, -1):
#         print(i, end="")
        
#     print()

for i in range(1, int(input())):
    print(i * (10**i - 1) // 9)