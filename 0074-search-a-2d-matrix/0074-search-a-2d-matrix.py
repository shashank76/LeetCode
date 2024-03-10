class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        for i in range(n):
            if target == matrix[i][0] or target == matrix[i][-1]:
                return True
            elif target < matrix[i][-1]:
                for i in matrix[i]:
                    if target == i:
                        return True
            elif target < matrix[i][0]:
                for i in matrix[i - 1]:
                    if target == i:
                        return True
        return False