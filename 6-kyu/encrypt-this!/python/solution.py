def enc_func(word):
    first_char = str(ord(word[0]))
    if len(word) == 1:
        return first_char
    last_letter = word[-1]
    if len(word) == 2:
        return first_char + last_letter
    return ''.join([first_char, last_letter, word[2:-1], word[1]])

def encrypt_this(text):
    if not text:
        return ''
    return ' '.join(map(enc_func, text.split()))