class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        out = 0
        i = 0
        while i < len(edges)-1:
            if edges[i][0] in edges[i+1]:
                out = edges[i][0]
            else:
                out = edges[i][1]
            i+=1
        return out
                
        