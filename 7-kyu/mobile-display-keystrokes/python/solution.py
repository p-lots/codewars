def mobile_keyboard(strng):
    lookup_table = {k: v for k, v in zip('abcdefghijklmnopqrstuvwxyz', '23423423423423423452342345')}
    return sum(int(lookup_table.get(ch, '1')) for ch in strng)
