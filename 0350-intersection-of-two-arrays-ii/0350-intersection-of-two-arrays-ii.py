class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = Counter(nums2)
        out = []
        for i in nums1:
            if i in nums2 and counter[i] > 0:
                out.append(i)
                counter[i] -= 1
        return out
        