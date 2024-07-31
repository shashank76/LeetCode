class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        cache = {}
        
        def helper(i):
            if i == len(books):
                return 0
            if i in cache:
                return cache[i]
            remWidth, maxHeight = shelfWidth, 0
            cache[i] = float("inf")
            
            for j in range(i, len(books)):
                w, h = books[j]
                if remWidth < w:
                    break
                remWidth-=w
                maxHeight = max(maxHeight, h)
                cache[i] = min(cache[i], helper(j+1)+maxHeight)
            return cache[i]
        
        return helper(0)
                
        