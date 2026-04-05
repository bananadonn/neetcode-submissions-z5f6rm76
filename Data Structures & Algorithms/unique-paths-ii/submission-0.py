class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        prevrow = [0] * cols

        for r in range(rows - 1, -1, -1):
            currow = [0] * cols
            if obstacleGrid[r][cols - 1] == 1:
                currow[cols -1] = 0
            else:
                if r == rows - 1:
                    currow[cols -1] = 1
                else:
                    currow[cols - 1] = prevrow[cols -1]

            for c in range(cols -2, -1, -1):
                if obstacleGrid[r][c] == 1:
                    currow[c] = 0
                    continue
                else:
                    currow[c] = currow[c + 1] + prevrow[c]
            prevrow = currow
        return prevrow[0]
                
            
        