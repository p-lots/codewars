def encode(message, key):
    message_list = [ord(letter) - ord('a') + 1 for letter in message]
    key_list = [int(n) for n in str(key)]
    return [n + key_list[i % len(key_list)] for (i, n) in enumerate(message_list)]