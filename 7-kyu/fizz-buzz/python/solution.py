def fizzbuzz_func(n):
    ret = ''
    if n % 3 == 0: ret += 'Fizz'
    if n % 5 == 0: ret += 'Buzz'
    if not ret: ret = n
    return ret

def fizzbuzz(n):
    return list(map(fizzbuzz_func, [i for i in range(1, n + 1)]))