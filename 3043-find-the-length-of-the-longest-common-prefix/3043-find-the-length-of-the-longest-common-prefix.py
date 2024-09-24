class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1
            
        prefixSet = set()
        
        for i in arr1:
            while i and i not in prefixSet:
                prefixSet.add(i)
                i = i // 10
        
        out = 0
        
        for i in arr2:
            while i and i not in prefixSet:
                i = i // 10
            if i:
                out = max(out, len(str(i)))
        return out