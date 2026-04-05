class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for num in nums:
            index = abs(num)
            if nums[index] < 0:
                return index
            else:
                nums[index] *= -1
        return -1
            
            