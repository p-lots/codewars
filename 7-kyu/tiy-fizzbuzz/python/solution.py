def is_vowel(letter):
    letter = letter.lower()
    return letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'

def tiy_fizz_buzz(string):
    ret = ''
    for char in string:
        if is_vowel(char):
            if char == char.upper():
                ret += 'Iron Yard'
            else:
                ret += 'Yard'
        elif char.isalpha() and char == char.upper():
            ret += 'Iron'
        else:
            ret += char
    return ret