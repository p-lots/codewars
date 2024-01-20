def is_vowel(letter):
    return letter.lower() in 'aeiou'

def tiy(letter):
    if is_vowel(letter) and letter.isupper():
        return 'Iron Yard'
    elif is_vowel(letter):
        return 'Yard'
    elif letter.isupper():
        return 'Iron'
    return letter

def tiy_fizz_buzz(strng):
    return ''.join(tiy(ch) for ch in strng)