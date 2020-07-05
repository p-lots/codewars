from string import ascii_uppercase

def title_to_number(title):
    title = list(title)
    power = 1
    base = len(ascii_uppercase)
    ret = 0
    while title:
        ret += (ascii_uppercase.index(title[-1]) + 1) * power
        power *= base
        title.pop()
    return ret