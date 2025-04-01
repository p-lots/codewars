def full_cycle(lst):
    visited = [False] * len(lst)
    curr_idx = 0
    num_seen = 0
    while True:
        num_seen += 1
        curr_idx = lst[curr_idx]
        visited[curr_idx] = True
        if all(visited):
            break
        elif num_seen == len(lst):
            return False
    return True
