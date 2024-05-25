class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        out = []
        cur = []
        wordDict = set(wordDict)
        def helper(i):
            if i == len(s):
                out.append(" ".join(cur))
                return out
            for j in range(i, len(s)):
                w = s[i:j+1]
                if w in wordDict:
                    cur.append(w)
                    helper(j+1)
                    cur.pop()
        helper(0)
        return out
        