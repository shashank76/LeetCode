class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {}
        x = 1
        for i in sorted(arr):
            if i not in ranks:
                ranks[i] = x
                x+=1
        for i, v in enumerate(arr):
            arr[i] = ranks[v]
        return arr
            
        