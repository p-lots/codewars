def second_symbol(strng, symbol):
    if not strng or symbol not in strng or strng.count(symbol) == 1:
        return -1
    first_idx = strng.find(symbol)
    return strng.find(symbol, first_idx + 1)
