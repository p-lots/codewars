from functools import reduce
from operator import mul

def strong_enough(earthquake, age):
    shockwaves = [sum(tremors) for tremors in earthquake]
    magnitude = reduce(mul, shockwaves, 1)
    original_strength = 1000
    current_strength = original_strength * 0.99 ** age
    return "Safe!" if current_strength >= magnitude else "Needs Reinforcement!"
