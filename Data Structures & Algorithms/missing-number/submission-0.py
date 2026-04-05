class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [-1] * (len(nums) + 1)

        for num in nums:
            arr[num] = num
        
        for i in range(len(arr)):
            if arr[i] < 0:
                return i