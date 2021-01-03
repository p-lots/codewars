def explode(s):
    return ''.join(ch * int(ch) for ch in s)