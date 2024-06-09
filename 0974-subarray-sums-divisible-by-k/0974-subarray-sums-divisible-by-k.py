class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        out = 0
        curSum = 0
        dictVal = { 0: 1 }
        for i in nums:
            curSum += i
            val = curSum % k
            out += dictVal.get(val, 0)
            dictVal[val] = 1 + dictVal.get(val, 0)
        return out
        