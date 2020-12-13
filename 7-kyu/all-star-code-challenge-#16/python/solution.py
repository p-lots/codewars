def no_repeat(strng):
    for ch in strng:
        if strng.count(ch) == 1:
            return ch