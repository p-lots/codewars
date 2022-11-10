from string import ascii_lowercase

def pass_the_door_man(word): 
    for lhs, rhs in zip(word, word[1:]):
        if lhs == rhs:
            return (ascii_lowercase.index(lhs) + 1) * 3
