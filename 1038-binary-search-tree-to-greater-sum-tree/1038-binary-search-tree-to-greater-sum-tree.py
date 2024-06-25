# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        out=0
        def helper(node):
            nonlocal out
            if node==None:
                return
            helper(node.right)
            out+=node.val
            node.val=out
            helper(node.left)
        helper(root)  
        return root 
        