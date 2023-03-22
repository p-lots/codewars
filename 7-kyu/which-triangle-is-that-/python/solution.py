def type_of_triangle(a, b, c): 
    if any(not isinstance(elem, int) for elem in [a, b, c]):
        return 'Not a valid triangle'
    shortest, mid, longest = sorted([a, b, c])
    if shortest + mid > longest:
        if a == b and b == c:
            return 'Equilateral'
        elif a == b or b == c or a == c:
            return 'Isosceles'
        return 'Scalene'
    return 'Not a valid triangle'
