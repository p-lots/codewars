def letters_to_numbers(s):
    total = 0
    for ch in s:
        if ch.islower():
            total += ord(ch) - ord('a') + 1
        elif ch.isupper():
            total += 2 * (ord(ch) - ord('A') + 1)
        elif ch.isdigit():
            total += int(ch)
    return total
