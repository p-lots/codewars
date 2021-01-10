def remove(s):
    return ' '.join(word for word in s.split() if word.count('!') != 1)
