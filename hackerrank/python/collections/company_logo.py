if __name__ == '__main__':
    s = input()

    occ = {}
    for ch in s:
        occ[ch] = occ.get(ch, 0) + 1

    sorted_items = sorted(occ.items(), key=lambda x: (-x[1], x[0]))

    for key, value in sorted_items[:3]:
        print(key, value)