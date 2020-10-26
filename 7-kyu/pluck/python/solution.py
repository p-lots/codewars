def pluck(objs, name): 
    return [elem.get(name, None) for elem in objs]