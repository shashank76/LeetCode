class Solution:
    def minimumLength(self, s: str) -> int:
        i, j = 0, len(s)-1
        while i < j and s[i] == s[j]:
            x = s[i]

            while i <= j and s[i] == x:
                i += 1

            while j > i and s[j] == x:
                j -= 1

        return j - i + 1
        