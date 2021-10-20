def t_area(t_str):
    t_str = t_str.replace('.', '')
    return ((t_str.count('\n') - 2) * len(max(t_str.split('\n'), key=lambda elem: elem.count(' ')))) * 0.5
