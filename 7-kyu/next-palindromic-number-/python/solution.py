def is_palindrome(n):
    return str(n) == str(n)[::-1]

def next_pal(val):
    if is_palindrome(val):
        val += 1
    while not is_palindrome(val):
        val += 1
    return val
