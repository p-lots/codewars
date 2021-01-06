def even_or_odd(s):
    even_sum = sum(int(n) for n in s if int(n) % 2 == 0)
    odd_sum = sum(int(n) for n in s if int(n) % 2 == 1)
    return 'Even is greater than Odd' if even_sum > odd_sum else 'Even and Odd are the same' if even_sum == odd_sum else 'Odd is greater than Even'