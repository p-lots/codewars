def reverse_and_mirror(s1, s2):
    invert_case = lambda s: ''.join(ch.upper() if ch.islower() else ch.lower() for ch in s)
    s1_transformed = invert_case(s1)
    s2_transformed = invert_case(s2)
    return f'{s2_transformed[::-1]}@@@{s1_transformed[::-1]}{s1_transformed}'
