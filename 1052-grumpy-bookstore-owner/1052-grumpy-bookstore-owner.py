class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied, not_satisfied = 0, 0
        maxVal = 0
        l, r = 0, 0
        
        while r < len(customers):
            if grumpy[r]:
                not_satisfied += customers[r]
            else:
                satisfied += customers[r]
            
            if minutes < r-l+1:
                if grumpy[l]:
                    not_satisfied -= customers[l]
                l+=1
            r+=1       
            maxVal= max(maxVal, not_satisfied)
        return satisfied + maxVal
            
        