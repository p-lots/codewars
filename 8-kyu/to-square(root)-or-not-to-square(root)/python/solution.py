def square_or_square_root(arr):
    is_perfect_square = lambda n: int(n ** 0.5) * int(n ** 0.5) == n
    return [num ** 0.5 if is_perfect_square(num) else num * num for num in arr]
