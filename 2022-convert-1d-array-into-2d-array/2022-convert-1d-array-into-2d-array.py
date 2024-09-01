class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        out = []
        if (m*n) == len(original):
            for i in range(m):
                cur = []
                x=i*n
                for j in range(n):
                    cur.append(original[x+j])
                out.append(cur)
        return out
            
        