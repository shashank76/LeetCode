class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = []
        cur = []
        nums.sort()
        def helper(i):
            if i >= len(nums):
                if cur not in out:
                    out.append(cur.copy())
                return out
            
            cur.append(nums[i])
            helper(i+1)
            cur.pop()
            helper(i+1)
            
        helper(0)
        return out
        