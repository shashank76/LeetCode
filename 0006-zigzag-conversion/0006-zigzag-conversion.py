class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s and numRows < 1:
            return ''
        
        if numRows == 1:
            return s

        out  = ''
        n = len(s)
        step = 2 * numRows - 2
        
        for i in range(numRows):
            for j in range(i, n, step):
                out += s[j]
                if 0 != i != numRows -1 and j + step - 2 * i < n:
                    out += s[j + step - 2 * i]
        return out
