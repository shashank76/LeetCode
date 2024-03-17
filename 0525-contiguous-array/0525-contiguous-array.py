class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zeros = once = 0
        dict_vals = {}
        out = 0 
        for i, val in enumerate(nums):
            if val == 0:
                zeros += 1
            else:
                once +=1
            if once - zeros not in dict_vals:
                dict_vals[once-zeros] = i
            
            if zeros == once:
                out = zeros + once
            else:
                idx= dict_vals[once - zeros]
                out = max(out, i-idx)  
        return out
        