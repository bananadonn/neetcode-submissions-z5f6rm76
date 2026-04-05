class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L = 0
        R = len(matrix) - 1

        while L <= R:
            M = (L + R) //2

            if target < matrix[M][0]:
                R = M - 1
            elif target > matrix[M][-1]:
                L = M + 1
            else:
                L = R + 1
            
        L = 0
        R = len(matrix[M]) -1

        while L <= R:

            mid = (L + R) //2

            if target < matrix[M][mid]:
                R = mid - 1
            elif target > matrix[M][mid]:
                L = mid + 1
            elif target == matrix[M][mid]:
                return True
        return False
        