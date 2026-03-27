def score_words(words):
    score = 0
    vowels = "aeiouy"
    
    for word in words:
        num_vowels = 0
        
        for char in word:
            if char in vowels:
                num_vowels += 1
        
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    
    return score


n = int(input())
words = input().split()

print(score_words(words))