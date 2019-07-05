def pop_shift(strng):
    halfway = len(strng) // 2
    if len(strng) % 2 == 1:
        return [ ''.join(reversed(strng[(halfway + 1):])), strng[:halfway], strng[halfway] ]
    else:
        return [ ''.join(reversed(strng[halfway:])), strng[:halfway], '' ]