def yoga(classroom, poses):
    ret = 0
    for row in classroom:
        row_sum = sum(row)
        ret += sum([sum([1 if val + row_sum >= pose else 0 for val in row]) for pose in poses])
    return ret