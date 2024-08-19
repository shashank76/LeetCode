class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        counted = {}
        
        def helper(c, p):
            if c == n:
                return 0
            if c > n:
                return 1000
            if (c, p) in counted:
                return counted[(c, p)]
            
            count1 = 1+helper(c+p, p)
            count2 = 2+helper(c+c, c)
            counted[(c, p)] = min(count1, count2)
            return counted[(c, p)]
            
        
        return 1+ helper(1, 1)
        