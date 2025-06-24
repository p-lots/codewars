def stone_pick(arr):
    cobble_count = arr.count('Cobblestone')
    stick_count = arr.count('Sticks') + arr.count('Wood') * 4
    return min(cobble_count // 3, stick_count // 2)
