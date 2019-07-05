def nb_dig(n, d):
    arr = [str(i * i) if str(d) in str(i * i) else '' for i in range(n + 1)]
    return sum(1 if len(num) > 0 and ch == str(d) else 0 for num in arr for ch in num)