def tail_swap(strngs):
    first_split = strngs[0].split(':')
    second_split = strngs[1].split(':')
    first_ret = first_split[0] + ':' + second_split[1]
    second_ret = second_split[0] + ':' + first_split[1]
    return [first_ret, second_ret]