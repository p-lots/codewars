def sing(): 
    ret = []
    for i in range(99, -1, -1):
        if i > 0:
            ret.append(f'{i} bottle{"s" if i != 1 else ""} of beer on the wall, {i} bottle{"s" if i != 1 else ""} of beer.')
            ret.append(f'Take one down and pass it around, {i - 1 if i > 1 else "no more"} bottle{"s" if i - 1 != 1 else ""} of beer on the wall.')
        else:
            ret.append(f'No more bottles of beer on the wall, no more bottles of beer.')
            ret.append(f'Go to the store and buy some more, 99 bottles of beer on the wall.')
    return ret
