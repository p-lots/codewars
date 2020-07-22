@countcalls
def replicate(times, number, lst=None):
    if lst is None:
        lst = []
    if times < 1:
        return lst
    lst.append(number)
    return replicate(times - 1, number, lst)