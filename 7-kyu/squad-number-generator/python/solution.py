def generate_number(squad, n):
    if n not in squad:
        return n
    for i in range(10):
        for j in range(10):
            ret = i * 10 + j
            if ret not in squad and i + j == n and ret != 90:
                return ret
    return None