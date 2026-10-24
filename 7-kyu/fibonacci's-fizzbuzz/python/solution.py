def fib(n):
    a, b = 1, 1
    count = 1
    yield a
    while count < n:
        a, b = b, a + b
        yield a
        count += 1
        
def fizz_buzz(n):
    match n % 3 == 0, n % 5 == 0:
        case False, False:
            return n
        case True, False:
            return 'Fizz'
        case False, True:
            return 'Buzz'
        case True, True:
            return 'FizzBuzz'

def fibs_fizz_buzz(n):
    return [fizz_buzz(x) for x in fib(n)]