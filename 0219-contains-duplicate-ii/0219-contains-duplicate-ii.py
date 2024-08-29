class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = set()
        i = 0
        for j in range(len(nums)):
            if j-i > k:
                visited.remove(nums[i])
                i+=1
            if nums[j] in visited:
                return True
            else:
                visited.add(nums[j])
                
        return False
        
        