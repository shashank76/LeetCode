class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        out = []
        def backtracking(i, cur, total):
            if total == target:
                out.append(cur.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            backtracking(i, cur, total+candidates[i])
            cur.pop()
            backtracking(i+1, cur, total)
            
        backtracking(0, [], 0)
        return out
        