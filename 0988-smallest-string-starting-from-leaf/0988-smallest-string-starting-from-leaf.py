# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        def dfs(node, val):
            if not node:
                return
            
            val = chr(ord('a') + node.val) + val
            
            if node.left and node.right:
                return min(
                    dfs(node.left, val),
                    dfs(node.right, val)
                )
            
            if node.right:
                return dfs(node.right, val)

            if node.left:
                return dfs(node.left, val)
            return val
            
        return dfs(root, '')