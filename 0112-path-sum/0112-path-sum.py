# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def backtracking(node, count):
            if not node:
                return False
            count += node.val
            
            if (not node.left) and (not node.right):
                return targetSum == count
            return backtracking(node.left, count) or backtracking(node.right, count)
            count -= node.val
        return backtracking(root, 0)
        
            
            
        