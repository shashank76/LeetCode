# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
            def addRow(root, val, depthRemaining):
                if root is None:
                    return

                if depthRemaining == 2:
                    root.left = TreeNode(val, left=root.left)
                    root.right = TreeNode(val, right=root.right)
                    return

                addRow(root.left, val, depthRemaining-1)
                addRow(root.right, val, depthRemaining-1)

            if depth == 1:
                return TreeNode(val, root)

            addRow(root, val, depth)
            return root
        