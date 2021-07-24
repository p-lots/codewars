from collections import Counter

def order_food(lst): 
    return Counter([dev['meal'] for dev in lst])
