class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dictVals = defaultdict(list)
        visited = set()
        
        for u, v in edges:
            dictVals[u].append(v)
            dictVals[v].append(u)
        
        def dfs(node, visited):
            if node == destination:
                return True
            visited.add(node)
            for val in dictVals[node]:
                if val not in visited:
                    if dfs(val, visited):
                        return True
            return False
        
        return dfs(source, visited)