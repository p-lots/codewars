from functools import reduce
from math import gcd

def final_attack_value(x, monster_list):
    return reduce(lambda acc, nxt: acc + (nxt if nxt < acc else gcd(acc, nxt)), monster_list, x)
