def color_2_grey(colors):
    avg = lambda *args: round(sum(args) / len(args))
    greyscale = []
    for row in colors:
        new_row = []
        for pixel in row:
            new_pixel = [avg(*pixel)] * 3
            new_row.append(new_pixel)
        greyscale.append(new_row)
    return greyscale
