class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        q = deque()
        minutes = 0
        fresh = 0
        neighbors = [(1,0),(0,1),(-1,0),(0,-1)] #add ,(-1,-1),(1,1),(1,-1),(-1,1) for diagonal support
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in neighbors:
                    if min(r+dr,c+dc) < 0 or r+dr == ROWS or c+dc == COLS or grid[r+dr][c+dc] == 0 or grid[r+dr][c+dc] == 2:
                        continue
                    grid[r+dr][c+dc] = 2
                    fresh -= 1
                    q.append((r+dr,c+dc))
            minutes += 1
        
        return minutes if fresh == 0 else -1