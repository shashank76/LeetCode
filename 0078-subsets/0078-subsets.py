class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        cur = []
        def helper(i):
            if i >= len(nums):
                out.append(cur.copy())
                return out
            
            cur.append(nums[i])
            helper(i+1)
            cur.pop()
            helper(i+1)
            
        helper(0)
        return out
        # out = [[]]
        # for i in nums:
        #     for j in range(len(out)):
        #         out.append(out[j]+[i])
        # return out
        