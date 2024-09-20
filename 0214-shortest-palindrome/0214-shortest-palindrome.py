class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        rev_s = s[::-1]
        s1 = s + "#" + rev_s
        
        maxStr = [0] * len(s1)
        
        for i in range(1, len(s1)):
            j = maxStr[i - 1]
            while j > 0 and s1[i] != s1[j]:
                j = maxStr[j - 1]
            if s1[i] == s1[j]:
                j += 1
            maxStr[i] = j
        
        maxLen = maxStr[-1]
        Val = rev_s[:len(s) - maxLen]
        
        return Val + s
        