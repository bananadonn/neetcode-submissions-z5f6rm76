class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1len, t2len = len(text1), len(text2)
        test = [[0 for _ in range(t2len + 1)] for _ in range(t1len + 1)]

        for i in range(t1len -1, - 1, -1):
            for j in range(t2len -1, -1, -1):

                if (text1[i] == text2[j]):
                    test[i][j] = 1 + test[i + 1][j + 1]
                else:
                    test[i][j] = max(test[i + 1][j], test[i][j + 1])
        return test[0][0]

        
        
        