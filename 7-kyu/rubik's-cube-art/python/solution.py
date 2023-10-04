def cube(n):
    def make_half(corner, edge, height):
        half = []
        line = ''
        for i in range(height):
            line += ' ' * (height - i - 1)
            line += corner * (i + 1)
            line += edge * n
            half.append(line)
            line = ''
        return half
    TOP_CORNER = '/\\'
    TOP_EDGE = '_\\'
    BOTTOM_CORNER = '\\/'
    BOTTOM_EDGE = '_/'
    top_half = make_half(TOP_CORNER, TOP_EDGE, n)
    bottom_half = make_half(BOTTOM_CORNER, BOTTOM_EDGE, n)
    return '\n'.join(top_half + bottom_half[::-1])
