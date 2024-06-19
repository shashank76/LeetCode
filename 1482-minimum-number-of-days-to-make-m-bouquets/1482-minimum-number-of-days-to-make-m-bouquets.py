class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # bloomDay.sort()
        # target = m*k
        # total = 0
        # i = 0
        # while i < len(bloomDay) -1:
        #     total = bloomDay[i] + bloomDay[i+1]
        #     if bloomDay[i] % target == 0:
        #         return bloomDay[i]
        #     elif total % target == 0:
        #         return total
        #     i+=1
        # return -1
        
        if m*k > len(bloomDay):
            return -1
        
        i, j = 1, max(bloomDay)
        
        while i < j:
            mid = (i+j) // 2
            cur = 0
            total = 0
            for day in bloomDay:
                
                if day > mid:
                    cur = 0 
                else:
                    cur += 1
                    
                if cur >= k:
                    cur = 0
                    total += 1
                if total == m:
                    break
            if total == m:
                j = mid
            else:
                i = mid+1
        return i