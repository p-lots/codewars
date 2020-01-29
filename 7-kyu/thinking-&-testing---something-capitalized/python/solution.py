def testit(s):
    return ' '.join(word[:-1] + word[-1].upper() for word in s.split())