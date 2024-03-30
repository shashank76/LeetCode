class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        dictVal = defaultdict(int)
        out = l1 = l2 = 0
        for r in range(len(nums)):
            dictVal[nums[r]] += 1
            
            while len(dictVal) > k:
                dictVal[nums[l2]] -=1
                if dictVal[nums[l2]] == 0:
                    dictVal.pop(nums[l2])
                l2+=1
                l1=l2
                
            while dictVal[nums[l2]] > 1:
                dictVal[nums[l2]] -=1
                l2+=1
                
            if len(dictVal) == k:
                out += l2-l1+1
        return out 
        