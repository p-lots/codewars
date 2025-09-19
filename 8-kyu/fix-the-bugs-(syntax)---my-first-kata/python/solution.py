def my_first_kata(a, b):
    if any(type(elem) != int for elem in [a, b]):
        return False
    return a % b + b % a
