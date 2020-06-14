def count_adjacent_pairs(st):
    st = st.lower().split()
    in_section = False
    ret = 0
    for first_word, second_word in zip(st, st[1:]):
        if first_word != second_word:
            in_section = False
        elif first_word == second_word and not in_section:
            in_section = True
            ret += 1
    return ret