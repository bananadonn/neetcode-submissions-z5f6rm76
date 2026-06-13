class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(abs(x))
        x_str = x_str[::-1]
        val = int(x_str) if x >= 0 else int(x_str) * -1
        return 0 if val > (2**31 - 1) or val < -1 * (2**31 - 1) else val