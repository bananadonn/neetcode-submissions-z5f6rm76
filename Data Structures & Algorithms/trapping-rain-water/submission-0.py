class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = 0
        maxright = 0
        water = 0
        l,r = 0, len(height) - 1

        while l < r:
            maxleft = max(maxleft, height[l])
            maxright = max(maxright, height[r])
            limiter = min(maxleft, maxright)

            if height[l] <= height[r]:
                capacity = limiter - height[l]
                if capacity > 0:
                    water += capacity
                l += 1
            else:
                capacity = limiter - height[r]
                if capacity > 0:
                    water += capacity
                r -= 1
        return water