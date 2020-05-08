def reverse(str):
    if not str:
        return ''
    str = list(str)
    last = str.pop()
    return last + reverse(str)