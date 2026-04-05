class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs( grid, r, c) -> None:
            if r < 0 or c < 0 or r>= ROWS or c >= COLS or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            dfs(grid, r + 1, c)
            dfs(grid, r - 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(grid, r,c)
        return islands