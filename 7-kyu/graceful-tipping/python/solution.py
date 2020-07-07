from math import ceil, floor, log10

def graceful_tipping(bill):
    tip = bill * 0.15
    total = ceil(tip + bill)
    if total < 10:
        return total
    mult = floor(log10(total)) - 1
    mod = 5 * (10 ** mult)
    diff = 0
    while ((total + diff) % mod) != 0:
        diff += 1
    return total + diff