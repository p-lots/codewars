def hex_color(codes):
    if len(codes) == 0:
        return 'black'
    red, green, blue = [int(code) for code in codes.split()]
    greatest = max(red, green, blue)
    if red == green == blue:
        if red > 0:
            return 'white'
        else:
            return 'black'
    elif red == green:
        if blue > red:
            return 'blue'
        return 'yellow'
    elif green == blue:
        if red > blue:
            return 'red'
        return 'cyan'
    elif red == blue:
        if green > blue:
            return 'green'
        return 'magenta'
    elif greatest == red:
        return 'red'
    elif greatest == green:
        return 'green'
    elif greatest == blue:
        return 'blue'
