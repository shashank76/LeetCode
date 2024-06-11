class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = Counter(arr1)
        remaining = sorted(list(counter.keys()))
        out = []
        for i in arr2:
            for j in range(counter[i]):
                out.append(i)
            remaining.remove(i) 
        for i in remaining:
            for j in range(counter[i]):
                out.append(i)
        return out
        