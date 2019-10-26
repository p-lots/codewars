def length(head, l=0): 
    if not head:
        return l
    return length(head.next, l + 1)