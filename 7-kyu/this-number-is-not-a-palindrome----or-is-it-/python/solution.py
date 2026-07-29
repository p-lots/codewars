def is_palindrome(n: int) -> bool:
    return f'{n:b}' == f'{n:b}'[::-1]