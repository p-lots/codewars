def split_and_merge(strng, separator):
    return ' '.join(separator.join(ch for ch in word) for word in strng.split())