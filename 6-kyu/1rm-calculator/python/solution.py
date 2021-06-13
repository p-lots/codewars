def epley(w, r):
    return w * (1 + r / 30)

def mcglothin(w, r):
    return 100 * w / (101.3 - 2.67123 * r)

def lombardi(w, r):
    return w * r ** 0.1

def calculate_1RM(w, r):
    if r < 1:
        return 0
    elif r == 1:
        return w
    return max(round(epley(w, r)), round(mcglothin(w, r)), round(lombardi(w, r)))
