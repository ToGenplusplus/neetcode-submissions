class Solution:
    def trap(self, heights: List[int]) -> int:
        
        if not heights:
            return 0


        left, right = 0, len(heights) - 1
        max_left, max_right = heights[left], heights[right]

        total = 0
        while left < right:

            if heights[left] < heights[right]:
                left += 1
                max_left = max(max_left, heights[left])
                total += max_left - heights[left]

            else:
                right -= 1
                max_right = max(max_right, heights[right])
                total += max_right - heights[right]

        return total