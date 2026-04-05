class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        
        for i in range(0, n + 1):
            count = 0
            while i > 0:
                if i % 2 == 1:
                    count += 1
                i = i//2
            arr.append(count)
        return arr    