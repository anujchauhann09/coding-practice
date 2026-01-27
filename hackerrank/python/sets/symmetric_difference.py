if __name__ == '__main__':
    n = int(input())
    s1 = set(map(int, input().split()))

    m = int(input())
    s2 = set(map(int, input().split()))

    ans = sorted(s1 ^ s2)  

    for x in ans:
        print(x)
