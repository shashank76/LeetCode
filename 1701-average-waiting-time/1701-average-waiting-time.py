class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waiting_time = 0
        finish_time = 0
        for i, j in customers:
            if finish_time < i:
                finish_time = i
            finish_time += j
            waiting_time += (finish_time - i )
        return waiting_time/len(customers)
        