n = int(input())
nums = list(map(int, input().split()))

print(all(n > 0 for n in nums) and any(str(n) == str(n)[::-1] for n in nums))