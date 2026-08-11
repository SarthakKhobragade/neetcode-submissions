class Solution:
    def trap(self, heights: List[int]) -> int:
        size = len(heights)
        max_to_left = [0] * (size+1)
        max_to_right = [0] * (size+1)

        for i in range(size):
            max_to_left[i] = max(max_to_left[i-1], heights[i])
            max_to_right[size-i-1] = max(max_to_right[(size-i)%size], heights[size-i-1])

        water = 0
        for i in range(1,size):
            curr_water = min(max_to_left[i-1],max_to_right[i+1]) - heights[i]
            if curr_water > 0:
                water += curr_water
        
        return water
