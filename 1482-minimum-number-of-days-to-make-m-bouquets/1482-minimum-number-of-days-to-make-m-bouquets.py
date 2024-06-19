class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def checkBloomDays(days):
            bouquets = 0
            count = 0

            for d in bloomDay:
                if d > days:
                    count = 0
                else:
                    count += 1
                    if count == k:
                        bouquets += 1
                        count = 0

            return bouquets >= m

        i, j = 1, max(bloomDay)

        while i < j:
            mid = (i+j) // 2
            if checkBloomDays(mid):
                j = mid
            else:
                i = mid + 1

        return i