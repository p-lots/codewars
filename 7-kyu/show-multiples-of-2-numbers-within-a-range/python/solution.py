def multiples(s1, s2, s3):
    return [n for n in range(1, s3) if n % s1 == 0 and n % s2 == 0]
