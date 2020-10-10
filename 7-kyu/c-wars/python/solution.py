def initials(name):
    name_split = name.lower().split()
    last = name_split[-1].title()
    ret = [n[0].upper() for n in name_split[:-1]]
    ret.append(last)
    return '.'.join(ret)