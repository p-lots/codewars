def element_location(begin: int, end: int, index: int, size: int) -> int:
    """Returns the address of an element in an array.
    Raises an IndexError if the element is not in the array.
    
    Unlike normal Python behavior, negative indexes are still considered to
    to start from the beginning of the array and are thus always out of bounds.
    """
    index_pos: int = begin + index * size
    if index < 0 or index_pos >= end:
        raise IndexError
    return index_pos
