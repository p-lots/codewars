def is_palindrome(n):
    if n < 10:
        return True
    n = str(n)
    return n == n[::-1]

def palindrome_chain_length(n):
    ret = 0
    while not is_palindrome(n):
        n += int(str(n)[::-1])
        ret += 1
    return ret
