def center(strng, width, fill=' '):
    if len(strng) > width:
        return strng
    fill_amt = width - len(strng)
    return ''.join([fill * ((fill_amt + (fill_amt % 2 == 1)) // 2), strng, fill * (fill_amt // 2)])
    