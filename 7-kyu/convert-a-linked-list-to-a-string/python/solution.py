def stringify(node):
    if node == None:
        return "None"
    nxt = node.next
    ret = [node.data]
    while nxt != None:
        ret.append(nxt.data)
        nxt = nxt.next
    ret.append("None")
    return ' -> '.join(str(item) if type(item) == int else item for item in ret)