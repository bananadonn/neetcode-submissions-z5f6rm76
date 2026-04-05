class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {} #store seen variables based on what row col and group they are in
        cols = {}
        grid = {}

        #go through each box in grid by index (row, col)
        for row in range(len(board)):
            for col in range(len(board[0])):
                num = board[row][col]
                if num == ".":
                    continue

                if row not in rows:
                    rows[row] = set()
                if num in rows[row]:
                    return False
                else: 
                    rows[row].add(num)

                if col not in cols:
                    cols[col] = set()
                if num in cols[col]:
                    return False
                else:
                    cols[col].add(num)
                
                if (row//3, col//3) not in grid:
                    grid[(row//3, col//3)] = set()
                if num in grid[(row//3, col//3)]:
                    return False
                else:
                    grid[(row//3, col//3)].add(num)
        return True