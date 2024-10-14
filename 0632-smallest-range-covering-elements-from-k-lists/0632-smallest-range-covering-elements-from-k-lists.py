class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minHeap = [(l[0], 1, i) for i, l in enumerate(nums)]
        heapify(minHeap)
        maxVal = max(l[0] for l in nums)
        out = [minHeap[0][0], maxVal]
        outLen = (out[1] - out[0], out[0])

        while True:
            curMin, nxtInd, numInd = heappop(minHeap)
            numArr = nums[numInd]
            if nxtInd == len(numArr):
                break
            nxtMin = numArr[nxtInd]
            heappush(minHeap, (nxtMin, nxtInd + 1, numInd))
            if nxtMin > maxVal:
                maxVal = nxtMin
            
            temp = [minHeap[0][0], maxVal]
            tempLen = (temp[1] - temp[0], temp[0])
            if tempLen < outLen:
                out = temp
                outLen = tempLen

        return out
        