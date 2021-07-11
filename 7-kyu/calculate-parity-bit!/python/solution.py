def check_parity(parity, bin_str):
    return 1 if bin_str.count('1') % 2 == (0 if parity == 'odd' else 1) else 0
