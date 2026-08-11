class Solution:
    def trap(self, heights: List[int]) -> int:
        size = len(heights)
        l, r = 0, size - 1

        max_left, max_right = heights[0], heights[size - 1]
        water = 0
        while l < r:
            if max_left <= max_right:
                l += 1
                max_left = max(max_left, heights[l])
                curr_water = max_left - heights[l]
            else:
                r -= 1
                max_right = max(max_right, heights[r])
                curr_water = max_right - heights[r]
            water += max(curr_water, 0)
        return water
