def find(n):
    return sum(number for number in range(1, n + 1) if number % 3 == 0 or number % 5 == 0)