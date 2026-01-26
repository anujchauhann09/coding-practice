def happiness(arr, s1, s2):
    counter = 0
    
    for x in arr:
        if x in s1:
            counter += 1
        elif x in s2:
            counter -= 1
        
    return counter

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    s1 = set(map(int, input().split()))
    s2 = set(map(int, input().split()))
    
    result = happiness(arr, s1, s2)
    print(result)