class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [0,1,1]
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        i = 3

        while i <= n:
            memo.append(memo[i - 1] + memo[i - 2] + memo[i - 3])
            i += 1
        
        return memo[-1]
    