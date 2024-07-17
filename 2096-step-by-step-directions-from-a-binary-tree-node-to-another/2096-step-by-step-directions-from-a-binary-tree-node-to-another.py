# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def dfs(node, path, target):
            if not node:
                return ""
            if node.val == target:
                return path
            path.append("L")
            out = dfs(node.left, path, target)
            if out:
                return out
            path.pop()
            path.append("R")
            out = dfs(node.right, path, target)
            if out:
                return out
            path.pop()
            return ""
            
        str_path = dfs(root, [], startValue)
        end_path = dfs(root, [], destValue)
        
        i = 0
        n = min(len(str_path), len(end_path))
        while i < n:
            if str_path[i] != end_path[i]:
                break
            i+=1
        out = ["U"] * len(str_path[i:]) + end_path[i:]  
        return "".join(out)
        