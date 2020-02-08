def house_numbers_sum(inp):
    zero_idx = inp.index(0)
    return sum(inp[:zero_idx])