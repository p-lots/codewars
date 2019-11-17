def make_lookup_table():
    remote = [
        [ 'a', 'b', 'c', 'd', 'e', '1', '2', '3' ],
        [ 'f', 'g', 'h', 'i', 'j', '4', '5', '6' ],
        [ 'k', 'l', 'm', 'n', 'o', '7', '8', '9' ],
        [ 'p', 'q', 'r', 's', 't', '.', '@', '0' ],
        [ 'u', 'v', 'w', 'x', 'y', 'z', '_', '/' ]
    ]
    ret = {}
    for i in range(len(remote)):
        for j in range(len(remote[i])):
            ret[remote[i][j]] = (i, j)
    return ret

def tv_remote(word):
    lookup = make_lookup_table()
    prev = 'a'
    ret = 0
    for letter in word:
        prev_pair = lookup[prev]
        curr_pair = lookup[letter]
        dist = (abs(prev_pair[0] - curr_pair[0]) + abs(prev_pair[1] - curr_pair[1]))
        ret += dist + 1
        prev = letter
    return ret