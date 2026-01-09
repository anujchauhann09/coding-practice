def count_substring(string, sub_string):
    counter = 0
    s1 = len(string)
    s2 = len(sub_string)
    
    for i in range(s1 - s2 + 1):
        j = i
        isMatching = True
        
        for k in range(s2):
            if string[j] != sub_string[k]:
                isMatching = False 
                break
                
            j = j + 1
            
        if(isMatching): 
            counter = counter + 1
    
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)