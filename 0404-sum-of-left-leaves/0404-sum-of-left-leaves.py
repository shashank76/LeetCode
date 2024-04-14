# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0  
        while root:  
            if root.left:  
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                
                if not predecessor.right:
                    predecessor.right = root  # temporary link 
                    root = root.left  
                else:
                    predecessor.right = None  
                    if predecessor == root.left and not predecessor.left:
                        res += predecessor.val 
                    root = root.right 
            else:
                root = root.right 
        return res

        