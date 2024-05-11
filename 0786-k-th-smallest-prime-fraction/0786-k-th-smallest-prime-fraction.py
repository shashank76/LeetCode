class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        if len(arr) > 2:
            res = []
            for i in range(len(arr)):
                for j in range(i + 1, len(arr)):
                    tmp = [arr[i] / arr[j], arr[i], arr[j]]
                    res.append(tmp)
            res.sort(key=lambda x: x[0])
            return [res[k - 1][1], res[k - 1][2]]
        else:
            return arr
        