def to_currency(price):
    price = list(str(price))[::-1]
    ret = ''
    counter = 0
    while price:
        ret += price[0]
        price.pop(0)
        counter += 1
        if price and counter == 3:
            ret += ','
            counter = 0
    return ret[::-1]
