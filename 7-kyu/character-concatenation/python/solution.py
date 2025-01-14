def char_concat(word):
    concat = [f'{word[i]}{word[len(word) - i - 1]}{i + 1}' for i in range(len(word) // 2)]
    return ''.join(concat)
