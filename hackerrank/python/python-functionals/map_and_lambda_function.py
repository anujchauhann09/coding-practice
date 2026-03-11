cube = lambda x: x**3

def fibonacci(n):
    ans = []
    a = 0
    b = 1
    
    for i in range(n):
        ans.append(a)
        a, b = b, a + b
        
    return ans
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))