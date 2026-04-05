class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob2(nums)-> int:
            rob1, rob2 = 0,0

            for i in nums:
                temp = max(rob1 + i, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        return max(rob2(nums[:-1]), rob2(nums[1:]))