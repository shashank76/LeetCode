class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj_nodes = defaultdict(list)
        for i, j in edges:
            adj_nodes[i].append(j)
            adj_nodes[j].append(i)
        
        edge_cnt = {}
        leaf_nodes = deque()
        
        for node, vals in adj_nodes.items():
            if len(vals) == 1:
                leaf_nodes.append(node)
            edge_cnt[node] = len(vals)
            
        while leaf_nodes:
            if n <= 2:
                return list(leaf_nodes)
            for i in range(len(leaf_nodes)):
                node = leaf_nodes.popleft()
                n-=1
                for x in adj_nodes[node]:
                    edge_cnt[x] -= 1
                    if edge_cnt[x] == 1:
                        leaf_nodes.append(x)
                        
                    
                    
                
            
            
            
        