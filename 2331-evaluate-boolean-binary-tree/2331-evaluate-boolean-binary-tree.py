# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if node is None:
                return True
            left = node.left
            right = node.right
            if left == None and right == None:
                if node.val == 0:
                    return False
                else:
                    return True 
            if node.val == 2:
                vals= dfs(left) or dfs(right)
            if node.val == 3:
                vals= dfs(left) and dfs(right)
            return vals
        return dfs(root)
        