class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        allnums = set()
        for num in nums:
            allnums.add(num)
        i = 1
        final = 0
        for num in nums:
            if (num - 1) not in allnums:
                i = 1
                while (num + i) in allnums:
                    i += 1
            final = max(final, i)
        return final
            