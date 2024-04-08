class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = Counter(students)
        for i in sandwiches:
            if count[i] > 0:
                count[i] -=1
            else:
                return sum(count.values())
        return sum(count.values())
        