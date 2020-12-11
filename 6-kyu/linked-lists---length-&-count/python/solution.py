class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node):
    if not node:
        return 0
    return 1 + length(node.next)

def count(node, data):
    ret = 0
    if not node:
        return ret
    if node.data == data:
        ret = 1
    return ret + count(node.next, data)
