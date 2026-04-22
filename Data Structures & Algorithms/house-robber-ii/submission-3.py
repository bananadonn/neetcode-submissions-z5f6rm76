class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.robhelper(nums[1:]), self.robhelper(nums[:-1]))


    def robhelper(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for house in nums:
            temp = max(house + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
        


        