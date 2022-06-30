def magic_sum(arr):
    return sum(n for n in arr if '3' in str(n) and n % 2 == 1)