class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(" ")
        n = len(arr) -1
        while n >= 0:
            if len(arr[n]) > 0:
                return len(arr[n])
            else:
                n-=1
        