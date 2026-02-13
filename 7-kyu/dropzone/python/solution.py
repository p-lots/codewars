from math import dist

def dropzone(p, dropzones):
    return min(dropzones, key=lambda point: dist(p, point))