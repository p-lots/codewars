def play_pass(s, n):
    ret = ''
    for i, ch in enumerate(s):
        if ch.isalpha():
            ord_ch = ord(ch) + n
            if ord_ch > 90:
                ord_ch -= 26
            str_ch = str(chr(ord_ch))
            str_ch = str_ch.upper() if i % 2 == 0 else str_ch.lower()
            ret += str_ch
        elif ch.isdigit():
            int_ch = 9 - int(ch)
            ret += str(int_ch)
        else:
            ret += ch
    return ret[::-1]