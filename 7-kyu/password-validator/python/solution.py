def password(strng):
    upper = any(ch.isupper() for ch in strng)
    lower = any(ch.islower() for ch in strng)
    number = any(ch.isdigit() for ch in strng)
    return upper and lower and number and len(strng) >= 8