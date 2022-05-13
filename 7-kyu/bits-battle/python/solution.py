def bits_battle(numbers):
    odds = [n for n in numbers if n % 2 == 1]
    evens = [n for n in numbers if n % 2 == 0 and n != 0]
    odd_ones_count = sum(f'{n:b}'.count('1') for n in odds)
    even_zeroes_count = sum(f'{n:b}'.count('0') for n in evens)
    return 'odds win' if odd_ones_count > even_zeroes_count \
        else 'evens win' if even_zeroes_count > odd_ones_count else 'tie'
