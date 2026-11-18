def left(strng: str, i: str | int = 1) -> str:
    if not i:
        return ''
    if isinstance(i, str):
        if i in strng:
            idx = strng.find(i)
            return strng[:idx]
        return ''
    return strng[:i]
    
def right(strng: str, i: str | int = 1) -> str:
    if not i:
        return ''
    if isinstance(i, str):
        if i in strng:
            idx = strng.rfind(i)
            return strng[idx + len(i):]
        return ''
    return strng[-i:]
