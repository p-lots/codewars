def odd_ones_out(numbers):
    return [n for n in numbers if numbers.count(n) % 2 == 0]