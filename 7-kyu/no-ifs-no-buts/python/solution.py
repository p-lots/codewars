def no_ifs_no_buts(a, b):
    idx = int(a > b) - int(a < b)
    comparative_phrase = ['equal to', 'greater than', 'smaller than'][idx]
    return f'{a} is {comparative_phrase} {b}'