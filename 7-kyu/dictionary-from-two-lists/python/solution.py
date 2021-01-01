def createDict(keys, values):
    while len(values) < len(keys):
        values.append(None)
    return dict(zip(keys, values))
