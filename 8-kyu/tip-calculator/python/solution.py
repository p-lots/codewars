from math import ceil

def calculate_tip(amount, rating):
    rating_lookup = {'terrible': 0, 'poor': .05, 'good': .1, 'great': .15, 'excellent': .2}
    rating = rating.lower()
    return 'Rating not recognised' if rating not in rating_lookup else ceil(amount * rating_lookup[rating])