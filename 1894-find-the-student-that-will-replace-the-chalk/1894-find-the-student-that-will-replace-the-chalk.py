class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sumVal = sum(chalk)
        val = k % sumVal
        out = 0
        i = 0
        while val >= 0:
            out = i
            if chalk[i] > val: 
                return out
            val-=chalk[i]
            i+=1
        return out
        