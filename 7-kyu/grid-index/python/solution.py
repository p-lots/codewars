def grid_index(grid, indexes):
    flattened = [elem for row in grid for elem in row]
    return ''.join(flattened[idx - 1] for idx in indexes)
