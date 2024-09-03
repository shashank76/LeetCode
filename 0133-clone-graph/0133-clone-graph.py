"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        cloneGraph = {}
        
        def dfs(node):
            if node in cloneGraph:
                return cloneGraph[node]
            newNode = Node(node.val)
            cloneGraph[node] = newNode
            for neiNode in node.neighbors:
                newNode.neighbors.append(dfs(neiNode))
            return newNode
        return dfs(node)
        