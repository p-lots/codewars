def stock_list(listOfArt, listOfCat):
    if not listOfArt or not listOfCat:
        return ''
    counts = {key: 0 for key in listOfCat}
    for item in listOfArt:
        code, stock_count = item.split(' ')
        stock_count = int(stock_count)
        if code[0] in counts.keys():
            counts[code[0]] += stock_count
    return ' - '.join(f'({key} : {val})' for key, val in counts.items())
