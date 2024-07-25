class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(nums):
            if len(nums) > 1:
                mid = len(nums)//2
                arr1 = nums[:mid]
                arr2 = nums[mid:]
                mergeSort(arr1)
                mergeSort(arr2)
                i, j, k = 0,0,0
                
                while i < len(arr1) and j < len(arr2):
                    if arr1[i] < arr2[j]:
                        nums[k] = arr1[i]
                        i+=1
                    else:
                        nums[k]=arr2[j]
                        j+=1
                    k+=1
                
                while i < len(arr1):
                    nums[k] = arr1[i]
                    i+=1
                    k+=1
                
                while j < len(arr2):
                    nums[k] = arr2[j]
                    j+=1
                    k+=1
                    
        mergeSort(nums)
        return nums
            
            
        