# from collections import OrderedDict

# N = int(input())
# ordered_occurrence = OrderedDict()

# for _ in range(N):
#     word = input()
#     ordered_occurrence[word] = ordered_occurrence.get(word, 0) + 1
    
# print(len(ordered_occurrence))
# for word, occ in ordered_occurrence.items():
#     print(occ, end=" ")

N = int(input())
words = {}

for _ in range(N):
    word = input()
    words[word] = words.get(word, 0) + 1

print(len(words))
print(*words.values())