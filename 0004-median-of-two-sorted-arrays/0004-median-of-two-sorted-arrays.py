class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        def find_meadin(l, r):
            i = (l + r) // 2
            j = mid - i - 2
            L1 = nums1[i] if i >= 0 else -inf
            L2 = nums1[i+1] if (i + 1) < m else inf
            R1 = nums2[j] if j >= 0 else -inf
            R2 = nums2[j+1] if (j + 1) < n else inf
            if L1 <= R2 and R1 <= L2:
                if (m + n) % 2:
                    print(L2, R2)
                    return min(L2, R2)
                return (max(L1, R1) + min(L2, R2)) / 2.0
            if L1 > R2:
                r = i - 1
                return find_meadin(l, r)
            else:
                l = i + 1
                return find_meadin(l, r)

        m = len(nums1)
        n = len(nums2)
        mid = (m + n) // 2
        l, r = 0, m - 1
        return find_meadin(l, r)
        