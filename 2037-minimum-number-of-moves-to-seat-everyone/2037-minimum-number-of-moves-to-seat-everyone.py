class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        i = 0
        out = 0
        
        def pos_arr(a, b):
            count = 0
            while a < b:
                a +=1
                count +=1
            return count
            
        while i < len(seats):
            if seats[i] < students[i]:
                out += pos_arr(seats[i], students[i])
            elif seats[i] > students[i]:
                out += pos_arr(students[i], seats[i])
            i+=1
        return out
        