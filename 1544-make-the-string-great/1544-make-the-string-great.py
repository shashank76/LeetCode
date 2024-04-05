class Solution:
    def makeGood(self, s: str) -> str:
        out =[]
        i = 0
        while i < len(s):
            if out and (out[-1] != s[i]) and (out[-1].lower() == s[i].lower()):
                out.pop()
            else:
                out.append(s[i])
            i+=1
        return "".join(out)
        
        