class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        cache = {}
        
        def helper(i):
            if i == len(s):
                return [""]
            if i in cache:
                return cache[i]
            out = []
            for j in range(i, len(s)):
                w = s[i:j+1]
                if w not in wordDict:
                    continue
                strs = helper(j+1)
                
                if not strs:
                    continue
                
                for x in strs:
                    vals = w
                    if x:
                        vals = vals + " " + x
                    out.append(vals)
            cache[i] = out
            return out
                
                    
        return helper(0)        