def build_section(char, char_repetitions, line_repetitions):
    line = [f'{char * char_repetitions}'] * line_repetitions
    return '\n'.join(line)

def generate_C(size):
    CHAR = 'C'
    TOTAL_HEIGHT = size * 5
    BORDER_WIDTH = size * 5
    BORDER_HEIGHT = size
    MIDDLE_WIDTH = size
    MIDDLE_HEIGHT = TOTAL_HEIGHT - BORDER_HEIGHT * 2
    BORDER = build_section(CHAR, BORDER_WIDTH, BORDER_HEIGHT)
    MIDDLE = build_section(CHAR, MIDDLE_WIDTH, MIDDLE_HEIGHT)
    ret = [BORDER, MIDDLE, BORDER]
    return '\n'.join(ret)