class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        edge_cnt = [0] * n
        label = 1
        out = 0
        
        for i, j in roads:
            edge_cnt[i]+=1
            edge_cnt[j]+=1
            
        for x in sorted(edge_cnt):
            out += label * x
            label +=1
        return out
        
        
        