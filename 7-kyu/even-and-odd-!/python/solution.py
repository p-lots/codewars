def even_and_odd(n): 
    return (int(''.join(str(num) for num in map(int, str(n)) if num % 2 == 0) or '0'), \
            int(''.join(str(num) for num in map(int, str(n)) if num % 2 == 1) or '0'))
