def calc(x):
    total1 = ''.join(str(ord(ch)) for ch in x)
    total2 = total1.replace('7', '1')
    return sum(map(int, total1)) - sum(map(int, total2))
