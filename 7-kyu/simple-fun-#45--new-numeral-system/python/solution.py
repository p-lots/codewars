from string import ascii_uppercase as alphabet

def new_numeral_system(number):
    idx = alphabet.index(number)
    sums = [f'{alphabet[i]} + {alphabet[idx - i]}' for i in range((idx // 2) + 1)]
    return sums
