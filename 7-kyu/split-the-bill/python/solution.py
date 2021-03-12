def split_the_bill(x):
    total = sum(x.values())
    number_of_guests = len(x.values())
    return {k: round(v - (total / number_of_guests), 2) for k, v in x.items()}
