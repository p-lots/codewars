def count_if(head, func):
    if head is None:
        return 0
    return (1 if func(head.data) else 0) + count_if(head.next, func)
