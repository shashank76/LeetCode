class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) -1
        count = 0
        while i<= j:
            remain = limit - people[j]
            count +=1
            j-=1
            if remain >= people[i]:
                i+=1
        return count
                
        