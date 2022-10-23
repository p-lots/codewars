def shades_of_grey(n):
    ret = [f'#{f"{i:02x}" * 3}' for i in range(1, 255)] if n > 0 else []
    return ret[:n]