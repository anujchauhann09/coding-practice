def swap_case(s):
    s = list(s)
    
    for i in range(len(s)):
        if 'a' <= s[i] <= 'z':
            s[i] = s[i].upper()
        elif 'A' <= s[i] <= 'Z':
            s[i] = s[i].lower()
            
    return ''.join(s)
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)