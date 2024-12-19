def find_spaceship(astromap):
    if not astromap:
        return 'Spaceship lost forever.'
    astromap_split = astromap.split('\n')
    for idx, row in enumerate(astromap_split):
        if 'X' in row:
            x = row.index('X')
            y = len(astromap_split) - idx - 1
            return [x, y]
    return 'Spaceship lost forever.'
