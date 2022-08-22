def comes_after(st, l):
    if l.lower() not in st.lower():
        return ''
    return ''.join(second for first, second in zip(st, st[1:]) if first.lower() == l.lower() and second.isalpha())
