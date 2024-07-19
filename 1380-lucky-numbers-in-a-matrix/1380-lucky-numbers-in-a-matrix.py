class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        val = float("-inf")
        for i in range(len(matrix)):
            val = max(val, min(matrix[i]))
        
        for i in range(len(matrix[0])):
            col_max = matrix[0][i]
            for j in range(len(matrix)):
                col_max = max(col_max, matrix[j][i])
            if col_max == val:
                return [col_max]
        return []
        