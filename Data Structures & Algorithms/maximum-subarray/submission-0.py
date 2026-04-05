class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        currsum = 0
        for i in nums:
            currsum = max(currsum,0) + i
            maxsum = max(maxsum,currsum)
        return maxsum 
        