class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        i, j = 0, rows-1
        
        while i<=j:
            row = (i+j)//2
            
            if target > matrix[row][-1]:
                i = row+1
            elif target < matrix[row][0]:
                j=row-1
            else:
                break
        if not (i<=j):
            return False
        row = (i+j)//2
        
        l, r = 0, cols-1
        while l <= r:
            m = (l+r)//2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m-1
            else:
                return True
        return False
        