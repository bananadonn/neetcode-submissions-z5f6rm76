class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numtoindex = {}
        for i in range(len(nums)):
            val2 = target - (nums[i])
            if val2 in numtoindex:
                return [numtoindex[val2], i]
            else:
                numtoindex[nums[i]] = i 

        return []