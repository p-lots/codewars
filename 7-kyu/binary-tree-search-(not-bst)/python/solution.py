from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right
        
    
def search(n: int, root: Optional[Node]) -> bool:
    """ Determines if a value is in a binary tree (NOT bst) """
    if root == None:
        return False
    elif root.value == n:
        return True
    elif root.left == None and root.right == None and root.value != n:
        return False
    return search(n, root.left) or search(n, root.right)
