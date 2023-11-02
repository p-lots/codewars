def alex_mistakes(number_of_katas, time_limit):
    MINUTES_PER_KATA = 6
    if number_of_katas * MINUTES_PER_KATA >= time_limit:
        return 0
    leftover = time_limit - number_of_katas * MINUTES_PER_KATA
    ret = 0
    time_for_pushups = 5
    while leftover - time_for_pushups >= 0:
        ret += 1
        leftover -= time_for_pushups
        time_for_pushups *= 2
    return ret
