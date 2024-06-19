class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        if len(nums) == 1:
            return [nums[:]]
        
        for i in nums:
            x = nums.pop(0)
            perms = self.permute(nums)
            for j in perms:
                j.append(x)
            out.extend(perms)
            nums.append(x)
        return out
            
        