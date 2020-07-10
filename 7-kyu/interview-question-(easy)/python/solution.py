from collections import Counter

def get_strings(city):
    city = [ch for ch in city.lower() if ch.isalpha()]
    city_counter = Counter(city)
    return ','.join(f"{k}:{v * '*'}" for k, v in city_counter.items())