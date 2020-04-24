def one(sq, fun):
    return sum(1 for item in sq if fun(item)) == 1