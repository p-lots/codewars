from collections import Counter

def strings_construction(a, b):
    times_found = 0
    b_lst = [ch for ch in b]
    while True:
        letter_found = False
        a_lst = [ch for ch in a]
        for letter in a:
            if a_lst and b_lst and letter in b_lst:
                b_lst.pop(b_lst.index(letter))
                a_lst.pop(a_lst.index(letter))
                letter_found = True
        if len(a_lst) == 0:
            times_found += 1
        elif not letter_found:
            break
    return times_found
