def alphabet_war(fight):
    letters_l = { 'w': 4, 'p': 3, 'b': 2, 's': 1 }
    letters_r = { 'm': 4, 'q': 3, 'd': 2, 'z': 1 }
    left_total = 0
    right_total = 0
    for ch in fight:
        if ch in letters_l:
            left_total += letters_l[ch]
        elif ch in letters_r:
            right_total += letters_r[ch]
    return 'Left side wins!' if left_total > right_total else 'Let\'s fight again!' if left_total == right_total else 'Right side wins!'