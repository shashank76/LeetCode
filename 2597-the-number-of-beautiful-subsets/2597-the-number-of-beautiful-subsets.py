class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        def helper(i, count):
            if i == len(nums):
                return 1
            
            out = helper(i+1, count)
            
            if not count[nums[i] + k] and not count[nums[i] -k]:
                count[nums[i]] += 1
                out += helper(i+1, count)
                count[nums[i]] -= 1
            return out
        
        return helper(0, defaultdict(int)) - 1
        