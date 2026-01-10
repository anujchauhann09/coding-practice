def print_rangoli(size):
    rev = []
    n = (size*2-1)*2-1
    
    for i in range(size+1):
        part1 = []
        for j in range (i):
            part1.append(chr(96+size-j))
            
        part2 = part1[::-1]
        result = part1 + part2[1::]
        
        if result:
            p = ("-".join(result)).center(n,"-")
            rev.append(p) 
            print(p)
            
    rev.reverse()
    print("\n".join(rev[1::]))

    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)