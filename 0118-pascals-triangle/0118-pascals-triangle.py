class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1]]
        
        for i in range(1,numRows):
            tmp = [0] + out[-1] + [0]
            nxtR = []
            for j in range(len(out[-1]) +1):
                nxtR.append(tmp[j] + tmp[j+1])
            out.append(nxtR)
        return out
        