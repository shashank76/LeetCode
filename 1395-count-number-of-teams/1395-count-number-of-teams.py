class Solution:
    def numTeams(self, rating: List[int]) -> int:
        out = 0
        for i in range(1, len(rating)-1):
            l1, r1 = 0, 0
            for j in range(i):
                if rating[j] < rating[i]:
                    l1+=1
            for j in range(i+1, len(rating)):
                if rating[j] > rating[i]:
                    r1+=1 
            out+= l1*r1
            l2 = i-l1
            r2 = len(rating) - i- 1-r1
            out+= l2*r2
        return out
                
        