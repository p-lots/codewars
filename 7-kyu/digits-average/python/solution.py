from math import ceil

def digits_average(input):
    if input < 10:
        return input
    ret = 0
    inp_str = str(input)
    for i in range(len(inp_str) - 1):
        avg = ceil((int(inp_str[i]) + int(inp_str[i + 1])) / 2)
        ret = ret * 10 + avg
    return digits_average(ret)