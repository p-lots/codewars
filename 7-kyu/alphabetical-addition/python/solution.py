def add_letters(*letters):
    if not letters:
        return 'z'
    total = sum(ord(letter) - ord('a') + 1 for letter in letters)
    if total % 26 == 0:
        return 'z'
    return chr(total % 26 + ord('a') - 1)