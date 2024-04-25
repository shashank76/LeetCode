class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0]*26
        
        for i in s:
            cur = ord(i) - ord('a')
            longest = 1
            for j in range(26):
                if abs(cur - j) <= k:
                    longest = max(longest, 1+dp[j])
            dp[cur] = max(dp[cur], longest)
        return max(dp)
                
        