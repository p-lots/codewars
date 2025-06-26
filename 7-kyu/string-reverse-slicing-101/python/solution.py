def reverse_slice(s):
    return [s[-(i + 1)::-1] for i in range(len(s))]