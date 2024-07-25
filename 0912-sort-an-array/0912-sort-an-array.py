class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(arr, l, m, r):
            arr1 = arr[l:m+1]
            arr2 = arr[m+1:r+1]
            
            i, j, k = 0,0,l
            
            while i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
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
        
        def devideArr(arr, i, j):
            if i == j:
                return arr
            mid = (i+j) // 2
            devideArr(arr, i, mid)
            devideArr(arr, mid+1, j)    
            mergeSort(arr, i, mid, j)
            return arr
        
        return devideArr(nums, 0, len(nums)-1)
            
            
        