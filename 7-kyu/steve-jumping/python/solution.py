from math import floor

def jumping(arr):
    if not arr:
        return f'jumped to the end with 20 remaining HP'
    health = 20
    lookup = {'D': 0, 'B': 0.5, 'H': 0.8, 'W': 1}
    curr_height = int(arr[0].split()[0])
    for i, block in enumerate(arr):
        distance, type = block.split(' ')
        distance = curr_height - int(distance)
        damage = max(0, floor((distance - 3.5) * (1 - lookup[type])))
        health -= damage
        curr_height -= distance
        if health <= 0:
            return f'died on {i}'
    return f'jumped to the end with {health} remaining HP'
