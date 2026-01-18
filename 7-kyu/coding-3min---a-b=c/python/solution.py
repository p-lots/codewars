def find_a_b(numbers, c):
    for i, x in enumerate(numbers):
        for j, y in enumerate(numbers):
            if x * y == c and i != j:
                return [x, y]
