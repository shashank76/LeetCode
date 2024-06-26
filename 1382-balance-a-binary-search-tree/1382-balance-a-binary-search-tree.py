# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        out=[]
        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            out.append(node.val)
            dfs(node.right)

        dfs(root)
        def tree(low,high):
            if low>high:
                return None
            mid=(low+high)//2
            root=TreeNode(out[mid])
            root.left=tree(low,mid-1)
            root.right=tree(mid+1,high)
            return root
        return tree(0,len(out)-1) 
        