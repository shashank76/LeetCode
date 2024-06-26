class Solution:
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1     
        return True 
    
    def partition(self, s: str) -> List[List[str]]:
        out, temp = [], []
        def dfs(i):
            if i < len(s):  
                j = i
                while j < len(s):
                    if self.isPalindrome(s, i, j):
                        temp.append(s[i:j+1])
                        dfs(j+1)
                        temp.pop()
                    j+=1
            else:
                out.append(temp.copy())
                return 
        dfs(0)
        return out
    
    
        