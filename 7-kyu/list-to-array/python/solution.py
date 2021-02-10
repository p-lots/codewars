def list_to_array(node):
    ret = []
    head = node
    while head:
        ret.append(head.value)
        head = head.next
    return ret