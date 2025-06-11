def smallest_integer(matrix):
    flattened = sorted([n for row in matrix for n in row])
    smallest = 0
    for n in flattened:
        if smallest == n:
            smallest += 1
    return smallest
