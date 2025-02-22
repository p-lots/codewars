def get_a_down_arrow_of(n):
    down_arrow = []
    for i in range(n):
        span = "".join(str(digit % 10) for digit in range(1, n - i + 1))
        line = " " * i + span[:-1] + span[::-1]
        down_arrow.append(line)
    return '\n'.join(down_arrow)