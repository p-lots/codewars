def isDigit(strng):
    try:
        ret = float(strng)
        return type(ret) == float
    except:
        return strng.isdigit()
    