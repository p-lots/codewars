def fibonacci(n: int) -> int:
    """Given a positive argument n, returns the nth term of the Fibonacci Sequence.
    """
    a, b = 0, 1
    count = 0
    while count < n:
        a, b = b, a + b
        count += 1
    return a
