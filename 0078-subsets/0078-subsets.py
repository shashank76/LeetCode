class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out, cur = [], []
        def backtracking(i):
            if i >= len(nums):
                out.append(cur.copy())
                return out
            
            cur.append(nums[i])
            backtracking(i+1)
            cur.pop()
            backtracking(i+1)
        backtracking(0)
        return out
        