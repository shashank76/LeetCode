class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        out = []
        
        def backtraking(cur, i, target):
            if target == 0:
                out.append(cur.copy())
                return 
            elif target < 0:
                return
            
            prev = -1
            for j in range(i, len(candidates)):
                if candidates[j] == prev:
                    continue
                cur.append(candidates[j])
                backtraking(cur, j+1, target-candidates[j])
                cur.pop()
                prev = candidates[j]
        backtraking([], 0, target)
        return out
                
        