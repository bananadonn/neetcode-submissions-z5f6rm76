class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sortnums = sorted(nums)
        return sortnums[-k]