class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        length = 0
        seen = set()

        for R in range(len(s)):
            if s[R] in seen:
                while s[L] != s[R]:
                    seen.remove(s[L])
                    L += 1
                seen.remove(s[L])
                L += 1
            seen.add(s[R])
            length = max(R - L + 1, length)
        return length 