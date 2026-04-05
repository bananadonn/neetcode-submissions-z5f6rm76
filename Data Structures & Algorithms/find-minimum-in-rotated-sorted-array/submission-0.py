class Solution:
    def findMin(self, nums: List[int]) -> int:
        smol = nums[0]

        for num in nums:
            smol = min(smol, num)

        return smol
        