class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0;
        length = 99999
        total = 0

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                length = min(R - L + 1, length)
                total -= nums[L]
                L += 1
        return 0 if(length == 99999) else length
        