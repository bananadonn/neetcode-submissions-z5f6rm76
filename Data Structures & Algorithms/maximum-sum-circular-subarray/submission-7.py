class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalmax, globalmin = nums[0], nums[0]
        currmax, currmin = 0,0
        total = 0

        for n in nums:
            currmax = max(currmax + n,n)
            currmin = min(currmin + n,n)
            total += n

            globalmax = max(globalmax, currmax)
            globalmin = min(globalmin, currmin)
        print(total - globalmin, globalmax, globalmin)
        return globalmax if globalmax < 0 else max(globalmax, (total - globalmin))