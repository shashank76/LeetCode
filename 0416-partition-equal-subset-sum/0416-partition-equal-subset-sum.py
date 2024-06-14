class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2 or sum(nums) % 2:
            return False
        target = sum(nums)//2
        dictVal = set()
        dictVal.add(0)
        for i in nums:
            newDictVal = dictVal.copy()
            for j in dictVal:
                if i+j == target:
                    return True
                newDictVal.add(i+j)
            dictVal = newDictVal
        return True if target in dictVal else False
        