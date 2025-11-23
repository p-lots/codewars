from itertools import islice

# https://docs.python.org/3/library/itertools.html#itertools.batched
def batched(iterable, n, *, strict=False):
    if n < 1:
        raise ValueError('n must be at least one')
    iterator = iter(iterable)
    while batch := tuple(islice(iterator, n)):
        if strict and len(batch) != n:
            raise ValueError('batched(): incomplete batch')
        yield batch

class Converter():
    @staticmethod
    def to_ascii(h):
        return ''.join(chr(int(f'{first}{second}', 16)) for first, second in batched(h, 2))
    
    @staticmethod
    def to_hex(s):
        return ''.join(f'{ord(ch):02x}' for ch in s)