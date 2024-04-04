def make_latin_square(n):
    numbers = list(range(1, n + 1))
    latin_square = []
    for i in range(n):
        rotated = numbers[i:] + numbers[:i]
        latin_square.append(rotated)
    return latin_square
