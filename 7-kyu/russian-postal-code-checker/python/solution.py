def zipvalidate(postcode):
    if not postcode:
        return False
    return postcode[0] not in '05789' and len(postcode) == 6 and all(n.isdigit() for n in postcode)