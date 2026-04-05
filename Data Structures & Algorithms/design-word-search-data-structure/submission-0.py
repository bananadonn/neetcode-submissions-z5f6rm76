class Trie:
    def __init__(self):
       self.children = {}
       self.word = False 
class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
            curr = curr.children[char]
        curr.word = True
    
    
    def search(self, word: str) -> bool:
        return self.searchhelper(word, self.root)

    def searchhelper(self, word: str, node) -> bool:
        curr = node

        for i, char in enumerate(word):
            if char == ".":
                for child in curr.children.values():
                    if self.searchhelper(word[i+1:], child):
                        return True
                return False
            if char not in curr.children:
                return False

            curr = curr.children[char]

        return curr.word

