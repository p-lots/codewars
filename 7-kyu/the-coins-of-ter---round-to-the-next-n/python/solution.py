def adjust(coin, price):
    adj = price
    while adj % coin != 0:
        adj += 1
    return adj
