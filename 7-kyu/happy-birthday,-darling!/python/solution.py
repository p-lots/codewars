def womens_age(n):
    base = n // 2 if n % 2 == 0 else (n - 1) // 2
    new_n = 20 if n % 2 == 0 else 21
    return f"{n}? That's just {new_n}, in base {base}!"