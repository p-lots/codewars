def alternate(n, first_value, second_value):
    values = [first_value, second_value]
    return [values[i % len(values)] for i in range(n)]
