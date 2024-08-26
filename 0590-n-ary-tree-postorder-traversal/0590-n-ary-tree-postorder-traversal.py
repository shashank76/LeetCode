"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        out =[]
        def helper(node):
            if not node:
                return
            if node.children:
                for chi in node.children:
                    helper(chi)
            out.append(node.val)
        helper(root)
        return out
        