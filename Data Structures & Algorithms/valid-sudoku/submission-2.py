class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        grid = {}

        for row in range(len(board)):
            for col in range(len(board[0])):
                num = board[row][col]

                if num == ".":
                    continue

                if row not in rows:
                    rows[row] = set()
                if num not in rows[row]:
                    rows[row].add(num)
                else:
                    return False
                
                if col not in cols:
                    cols[col] = set()
                if num not in cols[col]:
                    cols[col].add(num)
                else:
                    return False
                
                if ((row // 3, col // 3 ) not in grid):
                    grid[(row // 3, col // 3 )] = set()
                if num not in grid[(row // 3, col // 3 )]:
                    grid[(row // 3, col // 3 )].add(num)
                else:
                    return False
        return True
                
                