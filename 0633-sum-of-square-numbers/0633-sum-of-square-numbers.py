class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        nums = set()
        for i in range(int(math.sqrt(c)) + 1):
            nums.add(i*i)
            if (c - (i*i)) in nums:
                return True
        return False
        