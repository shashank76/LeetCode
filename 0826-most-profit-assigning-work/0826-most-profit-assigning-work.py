class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        totalProf = 0
        maxProf = 0
    
        for ability in sorted(worker):
            while jobs and ability >= jobs[0][0]:
                maxProf = max(maxProf, jobs.pop(0)[1])
        
            totalProf += maxProf
    
        return totalProf