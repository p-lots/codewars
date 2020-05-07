def poly_add(p1, p2):
    while len(p1) < len(p2):
        p1.append(0)
    while len(p2) < len(p1):
        p2.append(0)
    return [poly1 + poly2 for poly1, poly2 in zip(p1, p2)]