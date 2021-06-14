def rotate(strng):
    return [strng[i + 1:] + strng[:i + 1] for i in range(len(strng))]
