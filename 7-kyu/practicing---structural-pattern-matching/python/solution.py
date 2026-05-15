def matching(arg):
    match arg:
        case []:
            return 0
        case [elem]:
            return int(elem)
        case [x, *y, z]:
            try:
                return int(x) / int(z)
            except:
                return None
        case _:
            return None