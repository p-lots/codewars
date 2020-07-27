def sort_me(arr):
    return sorted(arr, key=lambda elem: str(elem)[-1] if type(elem) == int else elem[-1])