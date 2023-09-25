def convert_palindromes(numbers):
    is_palindrome = lambda number: number == int(str(number)[::-1])
    return [int(is_palindrome(number)) for number in numbers]
