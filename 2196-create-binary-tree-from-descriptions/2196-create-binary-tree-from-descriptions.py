# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()
        
        for par, chi, is_left in descriptions:
            children.add(chi)
            if par not in nodes:
                nodes[par] = TreeNode(par)
            if chi not in nodes:
                nodes[chi] = TreeNode(chi)
            
            if is_left:
                nodes[par].left = nodes[chi]
            else:
                nodes[par].right = nodes[chi]
            
        for p, c, l in descriptions:
            if p not in children:
                return nodes[p]