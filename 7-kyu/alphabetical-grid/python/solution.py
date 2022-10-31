import string
from itertools import islice, cycle

def grid(N):
    if N < 0:
        return None
    elif N == 0:
        return ''
    return '\n'.join(' '.join(islice(cycle(string.ascii_lowercase), i, i + N)) for i in range(N))