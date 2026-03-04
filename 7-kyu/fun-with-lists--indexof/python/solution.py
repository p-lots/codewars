def index_of(head, value):
    if not head:
        return -1
    idx = 0
    nxt = head
    while nxt:
        if nxt.data == value:
            return idx
        nxt = nxt.next
        idx += 1
    return -1
