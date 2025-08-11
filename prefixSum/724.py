class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = 0
        #PreComputing the total sum 
        for num in nums:
            totalSum += num
        
        #Finding Pivot idx
        leftSum = 0
        for idx,num in enumerate(nums):
            totalSum -= num
            if leftSum == totalSum :
                return idx        
            leftSum += num
        return -1


        