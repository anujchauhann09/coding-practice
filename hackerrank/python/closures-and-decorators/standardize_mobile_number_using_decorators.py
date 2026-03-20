def wrapper(f):
    def fun(l):
        res = []
        
        for num in l:
            num = num[-10:]
            first = num[:5]
            second = num[5:10]
            
            formatted = "+91 " + first + " " + second
            res.append(formatted)
            
        return f(res)
        
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


