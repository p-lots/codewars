def sc(apple):
    for x, row in enumerate(apple):
        for y, elem in enumerate(row):
            if elem == 'B':
                return (x, y)
