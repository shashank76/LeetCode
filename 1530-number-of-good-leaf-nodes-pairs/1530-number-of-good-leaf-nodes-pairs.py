# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        out = 0
        
        def dfs(node):
            nonlocal out
            if not node.left and not node.right:
                return [1]

            leftLeafs = dfs(node.left) if node.left else []
            rightLeafs = dfs(node.right) if node.right else []

            for x in leftLeafs:
                for y in rightLeafs:
                    out += x + y <= distance

            return [x + 1 for x in leftLeafs + rightLeafs if x < distance]
        
        dfs(root)
        return out
        