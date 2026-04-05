# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        s = 0
        while s <= n:
            mid = (s + n) // 2
            if guess(mid) > 0:
                s = mid + 1
            elif guess(mid) < 0:
                n = mid - 1
            elif guess(mid) == 0:
                return mid
        return 0
        
        