class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited = set()
        return self.pathhelper(grid, 0, 0, visited)

    def pathhelper(self, grid, r, c, visited) -> int:
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 1 or (r,c) in visited:
            return 0

        if r == len(grid) -1 and c == len(grid[0]) -1:
            return 1
        
        visited.add((r,c))

        count = 0
        count += self.pathhelper(grid, r + 1, c, visited)
        count += self.pathhelper(grid, r - 1, c, visited)
        count += self.pathhelper(grid, r, c + 1, visited)
        count += self.pathhelper(grid, r, c - 1, visited)

        visited.remove((r,c))
        return count


    
        