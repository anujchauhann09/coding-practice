if __name__ == '__main__':
    records = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    scores = []
    for name, score in records:
        if score not in scores:
            scores.append(score)

    scores.sort()
    secondLowest = scores[1]

    records.sort()
    for name, score in records:
        if score == secondLowest:
            print(name)
