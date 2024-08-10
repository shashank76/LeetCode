class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        def magicSquare(l1,l2,l3):
            if(len(set(l1+l2+l3))!=9):
                return False
            for i1 in range(3):
                 if(l1[i1]>9 or l2[i1]>9 or l3[i1]>9):
                    return False
            s1=l1[0]+l2[0]+l3[0]
            if(s1!=sum(l1) or s1!=sum(l2) or s1!=sum(l3)):
                 return False
            for i in range(1,3):
                if(s1!=l1[i]+l2[i]+l3[i]):
                    return False
            if(s1!=l1[0]+l2[1]+l3[2] or s1!=l1[2]+l2[1]+l3[0]):
                return False
            return True
        
        out = 0
        
        for i in range(len(grid)-2):
            gridVals = grid[i:]
            for j in range(len(gridVals[0])-2):
                l1 = gridVals[0][j:j+3]
                l2 = gridVals[1][j:j+3]
                l3 = gridVals[2][j:j+3]
                if(0 not in l1+l2+l3 and magicSquare(l1,l2,l3)==True):
                    out+=1
        return out
        