def olympic_ring(string):
    lookup_table = { 'A': 1, 'B': 2, 'D': 1,
        'O': 1, 'P': 1, 'Q': 1, 'R': 1, 'a': 1, 'b': 1,
        'd': 1, 'e': 1, 'g': 1, 'o': 1, 'p': 1, 'q': 1, }
    ret = 0
    for letter in string:
        if letter in lookup_table:
            ret += lookup_table[letter]
    if ret // 2 > 3:
        return 'Gold!'
    elif ret // 2 == 3:
        return 'Silver!'
    elif ret // 2 == 2:
        return 'Bronze!'
    else:
        return 'Not even a medal!'