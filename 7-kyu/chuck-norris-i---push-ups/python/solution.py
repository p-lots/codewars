def chuck_push_ups(st):
    if type(st) != str or len(st) == 0:
        return 'FAIL!!'
    numbers = [''.join(ch for ch in elem if ch == '1' or ch == '0') for elem in st.split()]
    numbers = list(filter(lambda elem: len(elem) > 1, numbers))
    if len(numbers) < 1:
        return 'CHUCK SMASH!!'
    return max(int(elem, 2) for elem in numbers)
