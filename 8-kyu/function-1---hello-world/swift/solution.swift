def greet():
    phrase = [ 72, 69, 76, 76, 79, 0, 87, 79, 82, 76, 68, 1 ]
    return ''.join(chr(n + 32) for n in phrase)