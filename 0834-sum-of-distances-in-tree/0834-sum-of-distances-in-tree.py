class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges: 
            graph[u].append(v)
            graph[v].append(u)
        
        nodes_count = [1] * n
        ans = [0] * n

        def dfs_root_node(node = 0, parent = None):
            for child in graph[node]:
                if child == parent: 
                    continue

                dfs_root_node(child, node)

                nodes_count[node] += nodes_count[child]

                ans[node] += ans[child] + nodes_count[child]
        
        def dfs_other_node(node=0, parent=None):
            for child in graph[node]:
                if child == parent: 
                    continue
                
                ans[child] = ans[node] - nodes_count[child] + (n - nodes_count[child])
                dfs_other_node(child, node)

        dfs_root_node()
        dfs_other_node()

        return ans
        