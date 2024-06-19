class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # nums = set()
        # for i in range(int(math.sqrt(c)) + 1):
        #     nums.add(i*i)
        #     if (c - (i*i)) in nums:
        #         return True
        # return False
        i, j = 0, int(math.sqrt(c))
        
        while i<=j:
            val = i*i + j*j
            if val == c:
                return True
            elif val < c:
                i+=1
            else:
                j-=1
        return False
        