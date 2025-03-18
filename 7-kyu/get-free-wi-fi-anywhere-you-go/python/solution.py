def nonstop_hotspot(area):
    area_split = [a if 'P' in a else '' for a in area.split('#')]
    return sum(a.count('*') for a in area_split)
    