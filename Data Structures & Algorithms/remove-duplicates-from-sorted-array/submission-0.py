class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 1
        for i in range(0,len(nums) -1):
            if nums[i] != nums[i+1]:
                nums[unique] = nums[i+1]
                unique += 1
            else:
                continue
        return unique
