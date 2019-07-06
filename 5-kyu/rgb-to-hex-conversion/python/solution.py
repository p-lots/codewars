def clamp(n):
    return min(max(n, 0), 255)

def rgb(r, g, b):
    r, g, b = clamp(r), clamp(g), clamp(b)
    return '{0:02x}{1:02x}{2:02x}'.format(r, g, b).upper()