class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQ = collections.deque()
        maxQ = collections.deque()
        l = r = 0
        out = 0
        while r < len(nums):
            while minQ and minQ[-1] > nums[r]:
                minQ.pop()
            while maxQ and maxQ[-1] < nums[r]:
                maxQ.pop()
            
            minQ.append(nums[r])
            maxQ.append(nums[r])

            while (maxQ[0] - minQ[0]) > limit:
                if nums[l] == minQ[0]:
                    minQ.popleft()
                if nums[l] == maxQ[0]:
                    maxQ.popleft()
                l+=1
            out = max(out, r-l+1)
            r+=1
        return out
        