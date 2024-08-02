class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total_1count = nums.count(1)
        cur_1count = max_1count = 0
        i = 0
        for j in range(2*n):
            if nums[j%n]==1:
                cur_1count+=1
            if j -i+1 > total_1count:
                cur_1count-=nums[i%n]
                i+=1
            max_1count = max(max_1count, cur_1count)
        return total_1count - max_1count
                
        