def prefill(n, v=None):
    try:
        n = int(n)
    except:
        raise TypeError(f"{n} is invalid")
    if n < 1:
        return []
    return [v] * n