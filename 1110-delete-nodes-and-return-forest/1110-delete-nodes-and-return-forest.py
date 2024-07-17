# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if root.val not in to_delete:
            ans = [root]
        else:
            ans = [] 
        
        def postorder(node):
            if not node:
                return 

            postorder(node.left)      
            postorder(node.right) 
            
            if node.left and node.left.val in to_delete:
                if node.left.left:
                    ans.append(node.left.left) 
                if node.left.right:
                    ans.append(node.left.right) 
                node.left = None 
                
            if node.right and node.right.val in to_delete:
                if node.right.left:
                    ans.append(node.right.left)
                if node.right.right:
                    ans.append(node.right.right) 
                    
                node.right = None 
                        
        postorder(root)
        
        if root.val in to_delete:
            if root.left:
                ans.append(root.left) 
            if root.right:
                ans.append(root.right) 
                
        return ans
        