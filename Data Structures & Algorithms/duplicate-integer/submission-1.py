class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set()
        for i in nums:
            if i in numset:
                return True
            else:
                numset.add(i)
        return False
        