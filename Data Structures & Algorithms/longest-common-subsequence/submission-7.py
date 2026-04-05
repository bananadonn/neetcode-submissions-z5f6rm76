class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.memo = {}
        return self.helper(text1, text2, 0, 0)

    def helper(self, text1: str, text2: str, i: int, j: int) -> int:
        if i >= len(text1) or j >= len(text2):
            return 0
        
        if (i,j) in self.memo:
            return self.memo[(i,j)]

        if text1[i] == text2[j]:
            return 1 + self.helper(text1, text2, i + 1, j + 1)
        else:
            ans = max(self.helper(text1, text2, i + 1, j),
            self.helper(text1, text2, i, j + 1))
        
        self.memo[(i,j)] = ans
        return ans
            
            

        
        