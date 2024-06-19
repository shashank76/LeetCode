class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        
        def backtraking(cur, i, total):
            if total == target:
                out.append(cur.copy())
                return
            if i >= len(candidates) or target < total:
                return
            
            cur.append(candidates[i])
            backtraking(cur, i, total+candidates[i])
            cur.pop()
            backtraking(cur, i+1, total)
        backtraking([], 0, 0)
        return out
        