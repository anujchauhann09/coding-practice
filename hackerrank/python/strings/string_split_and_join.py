def split_and_join(line):
    ls = line.split(' ')
    line = '-'.join(ls)
    
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)