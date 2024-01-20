# input is an unsorted list of 3 positive integers
def pythagorean_triple(integers):
    # return True if it is possible to form a Pythagorean triple with the 3 integers
    # return False if it is not possible
    a, b, c = sorted(integers)
    return a ** 2 + b ** 2 == c ** 2