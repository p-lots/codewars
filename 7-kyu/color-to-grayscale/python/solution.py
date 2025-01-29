def rgb_to_grayscale(color):
    red = int(color[1:3], 16)
    green = int(color[3:5], 16)
    blue = int(color[5:], 16)
    luminance = round(0.299 * red + 0.587 * green + 0.114 * blue)
    return '#' + f'{luminance:02X}' * 3
