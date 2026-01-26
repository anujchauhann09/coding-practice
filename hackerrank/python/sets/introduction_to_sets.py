def average(array):
    st = set(array)
    s = sum(st)
    
    return (s / len(st))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)