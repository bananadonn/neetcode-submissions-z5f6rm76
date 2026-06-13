class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        i = 1
        if len(nums) == 1:
            return True
        while i < len(nums):
            print(i)
            if nums[i] % 2 == nums[i - 1] % 2:
                return False
            i += 1
        return True
        