class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        seen = set()
        self.color = color
        self.og = image[sr][sc]
        self.helper(image, sr, sc, seen)
        return image
    def helper(self, image, r, c, seen):
        COL, ROW = len(image[0]), len(image)
        if min(r,c) < 0 or r >= ROW or c >= COL or (r,c) in seen or image[r][c] != self.og:
            return
        else:
            image[r][c] = self.color
            seen.add((r,c))

            self.helper(image, r + 1, c, seen)
            self.helper(image, r - 1, c, seen)
            self.helper(image, r, c + 1, seen)
            self.helper(image, r, c - 1, seen)