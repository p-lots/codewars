def getCount(inputStr):
    num_vowels = 0
    for ch in inputStr:
        if ch in 'aeiou':
            num_vowels += 1
    return num_vowels