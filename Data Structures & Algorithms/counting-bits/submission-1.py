class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        
        for i in range(n + 1):
            n = i
            count = 0
            while n > 0:
                if n & 1 == 1:
                    count += 1
                n = n >> 1
            arr.append(count)
        return arr
