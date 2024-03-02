class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        out = []
        i, j = 0, len(nums)-1
        while i<=j:
            if nums[i]**2 > nums[j]**2:
                out.append(nums[i]**2)
                i+=1
            else:
                out.append(nums[j]**2)
                j-=1
        return out[::-1]
        