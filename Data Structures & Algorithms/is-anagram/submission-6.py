class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        wordmap = {}
        for char in s:
            if char not in wordmap:
                wordmap[char] = 1
            else:
                wordmap[char] += 1
        for char in t:
            if char in wordmap:
                wordmap[char] -= 1
                if wordmap[char] <= 0:
                    del wordmap[char]
        if not wordmap:
            return True
        else:
            return False
