def is_eviternity(n):
    for ch in n:
        if ch not in '358':
            return False
    return n.count('8') >= n.count('5') >= n.count('3')

def solve(a, b):
    return sum(is_eviternity(str(n)) for n in range(a, b))
