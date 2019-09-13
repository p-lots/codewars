def is_palindrome(strng):
    if type(strng) == int:
        strng = [int(digit) for digit in str(strng)]
    return strng == strng[::-1]