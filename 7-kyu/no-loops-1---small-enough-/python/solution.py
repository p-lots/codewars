def small_enough(a, limit): 
    return small_enough_helper(a, limit, True)

def small_enough_helper(a, limit, prev):
    if not a:
        return prev
    if a[0] > limit:
        prev = False
        return prev
    return small_enough_helper(a[1:], limit, prev)