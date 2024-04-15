# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        totalSum = 0
        def sumRootToLeaf(root, currSum):
            nonlocal totalSum
            if not root:
                return
            if not root.left and not root.right:
                totalSum += (currSum*10) + root.val
                return
            sumRootToLeaf(root.left, (currSum*10) + root.val)
            sumRootToLeaf(root.right, (currSum*10) + root.val)

        sumRootToLeaf(root, 0)
        return totalSum