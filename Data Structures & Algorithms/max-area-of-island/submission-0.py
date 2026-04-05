class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        largest = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(grid, r, c) -> int:
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            return ( 1 + 
            dfs(grid, r + 1, c) +
            dfs(grid, r - 1, c) + 
            dfs(grid, r, c + 1) +
            dfs(grid, r, c - 1)
            )


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    largest = max(largest, dfs(grid, r, c))
        return largest