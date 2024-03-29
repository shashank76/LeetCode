class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        x = strs[0]
        for i in strs:
            while i.startswith(x) == False:
                x = x[:-1]
        return x