def histogram(results):
    ret = ''
    curr_side = len(results)
    for result in results[::-1]:
        ret += str(curr_side) + "|"
        if result == 0:
            ret += "\n"
            curr_side -= 1
            continue
        ret += ''.join('#' for _ in range(result)) + ' ' + str(result) + '\n'
        curr_side -= 1
    return ret