class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        def helper(i, cur):
            if i >= len(nums):
                out.append(cur.copy())
                return out
            
            cur.append(nums[i])
            helper(i+1, cur)
            cur.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            helper(i+1, cur)
            
        helper(0, [])
        return out
#         out = []
#         cur = []
#         nums.sort()
#         def helper(i):
#             if i >= len(nums):
#                 if cur not in out:
#                     out.append(cur.copy())
#                 return out
            
#             cur.append(nums[i])
#             helper(i+1)
#             cur.pop()
#             helper(i+1)
            
#         helper(0)
#         return out

        