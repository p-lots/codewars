def score_per_lines_cleared(lines_cleared, level) -> int:
    level += 1
    if lines_cleared == 1:
        return 40 * level
    elif lines_cleared == 2:
        return 100 * level
    elif lines_cleared == 3:
        return 300 * level
    elif lines_cleared == 4:
        return 1200 * level
    return 0

def get_score(arr) -> int:
    ret = 0
    level = 0
    total_lines = 0
    for lines_cleared in arr:
        ret += score_per_lines_cleared(lines_cleared, level)
        total_lines += lines_cleared
        level = total_lines // 10
    return ret