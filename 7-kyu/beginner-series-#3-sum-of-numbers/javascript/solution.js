def get_sum(a,b):
    smaller, larger = min(a, b), max(a, b)
    return sum(n for n in range(smaller, larger + 1))