import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        L = 1
        R = max(piles)

        while L <= R:
            
            mid = (L + R) // 2
            if self.isvalid(piles,h,mid) == False:
                L = mid + 1
            elif self.isvalid(piles,h,mid)==True:
                R = mid - 1
        return L


    def isvalid(self, arr: List[int], h: int, x) -> bool:
            sum = 0 
            for i in arr:
                sum += (math.ceil(i / x))
            if sum <= h:
                return True
            else:
                return False
        