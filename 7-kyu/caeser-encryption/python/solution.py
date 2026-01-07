def caeser(message, key):
    # ((ord('t') - ord('a') + 25) % 26) + ord('a')
    return ''.join(chr((ord(ch.lower()) - ord('a') + key) % 26 + ord('a')) if ch.isalpha() else ch for ch in message).upper()

