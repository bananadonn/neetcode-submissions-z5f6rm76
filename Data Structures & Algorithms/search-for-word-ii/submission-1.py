class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self,word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        res, visit = set(), set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, curr, word):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visit or board[r][c] not in curr.children:
                return
            
            visit.add((r,c))
            word += board[r][c]
            curr = curr.children[board[r][c]]
            if curr.isWord:
                res.add(word)

            dfs(r + 1, c, curr, word)
            dfs(r - 1, c, curr, word)
            dfs(r, c + 1, curr, word)
            dfs(r, c - 1, curr, word)
            visit.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root, '')
        return list(res)