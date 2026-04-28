class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)
        while r <= len(s2):
            if self.checkPermutation(s1, s2[l:r]):
                return True
            l += 1
            r += 1
        return False

    def checkPermutation(self, s1: str, s2: str):
        freq2 = {}
        freq1 = {}
        for char2 in s2:
            freq2[char2] = 1 + freq2.get(char2, 0)
        for char1 in s1:
            freq1[char1] = 1 + freq1.get(char1,0)
        return freq1 == freq2