class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        dictVal = defaultdict(int)
        out = count = 0
        for i in range(len(nums)):
            dictVal[nums[i]] += 1
            while dictVal[nums[i]] > k:
                dictVal[nums[count]] -= 1
                count +=1
            out = max(out, i-count+1)
        return out 
        