import random

def random_case(x):
    return ''.join(ch.upper() if random.random() > 0.5 else ch.lower() for ch in x)
