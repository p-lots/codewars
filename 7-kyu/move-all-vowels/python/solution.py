def move_vowels(strng):
    vowels = ''
    cons = ''
    for ch in strng:
        if ch in 'aeiou':
            vowels += ch
        else:
            cons += ch
    return cons + vowels