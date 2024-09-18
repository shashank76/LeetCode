class Solution:
    def largestNumber(self, nums: List[int]) -> str:                 
        def calVal(i, j):
            if i + j > j + i:
                return 1
            elif i == j:
                return 0
            else:
                return -1

        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(calVal), reverse=True)
        return "".join(nums).lstrip("0") or "0"