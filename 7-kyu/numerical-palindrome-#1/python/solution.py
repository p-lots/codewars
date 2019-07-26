def palindrome(num):
    if type(num) != int or num < 0:
        return 'Not valid'
    return str(num) == str(num)[::-1]