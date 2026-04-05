class Solution:
    def uniquePaths(self, r: int, c: int) -> int:
        prevrow = [0] * c

        for i in range(r-1, -1, -1):
            currrow = [0] * c
            currrow[c-1] = 1
            for index in range(c-2, -1,-1):
                currrow[index] = currrow[index + 1] + prevrow[index]
            prevrow = currrow
        return prevrow[0] 