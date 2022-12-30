def duplicate_elements(m, n):
    return any(x == y for x in m for y in n)