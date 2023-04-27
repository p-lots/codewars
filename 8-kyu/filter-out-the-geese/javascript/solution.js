geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    ret = []
    for bird in birds:
        if bird not in geese:
            ret.append(bird)
    return ret