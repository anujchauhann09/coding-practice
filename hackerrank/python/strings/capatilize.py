def solve(s):
    result = ""
    capitalize = True

    for ch in s:
        if ch == " ":
            result += ch
            capitalize = True
        else:
            if capitalize:
                result += ch.upper()
                capitalize = False
            else:
                result += ch

    return result

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
