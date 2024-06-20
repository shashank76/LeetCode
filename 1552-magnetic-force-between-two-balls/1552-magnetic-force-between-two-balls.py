class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def minForce(mid, arr, balls):
            prev = arr[0]
            balls -= 1
            for b in arr[1:]:
                if abs(b - prev) >= mid:
                    balls -= 1
                    prev = b
                if balls == 0:
                    return True
            
            return balls == 0
        
        
        l = 1
        r = max(position) - min(position)
        while l <= r:
            mid = l + (r - l) // 2
            if minForce(mid, position, m):
                l = mid + 1
            else:
                r = mid - 1
        
        return l - 1
                
        