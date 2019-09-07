def solve(s):
    ret = ''
    greatest = 0
    for ch in s:
        if ret and ch.isalpha():
            greatest = max(int(ret), greatest)
            ret = ''
        elif ch.isdigit():
            ret += ch
    if ret:
        greatest = max(int(ret), greatest)
    return greatest