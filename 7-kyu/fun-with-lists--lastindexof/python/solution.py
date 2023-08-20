def last_index_of(head, search_val, curr=0, found=-1):
    if head is None:
        return found
    if search_val == head.data:
        found = curr
    if head.next is None:
        return found
    return last_index_of(head.next, search_val, curr + 1, found)
