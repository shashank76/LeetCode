class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        out = 0
        l1 = l2 = count = -1

        for i, val in enumerate(nums) :
            if not minK <= val <= maxK:
                l2 = i

            if val == minK:
                l1 = i

            if val == maxK:
                count = i

            out += max(0, min(l1, count) - l2)

        return out
        