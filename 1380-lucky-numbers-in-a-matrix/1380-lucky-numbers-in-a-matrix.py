class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        out = []
        row_min = []
        for i in range(len(matrix)):
            row_min.append(min(matrix[i]))
        
        for i in range(len(matrix[0])):
            col_max = matrix[0][i]
            for j in range(len(matrix)):
                col_max = max(col_max, matrix[j][i])
            if col_max in row_min:
                out.append(col_max)
            
        return out
        