class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = []
        i = 0
        for num in nums:
            if target - num in vals:
                return[nums.index(target - num), i]
            else:
                vals.append(num)
            i += 1