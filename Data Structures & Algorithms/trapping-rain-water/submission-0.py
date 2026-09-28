class Solution:
    def trap(self, height: List[int]) -> int:
        """
            area = l x w

            looking for max area trapped BETWEEN bars
            examples

            height = [0,2,0,3,1,0,1,3,2,1] -> 9

            [0,2,0,3,1,0,1,3,2,1]
            
        """

        if not height:
            return 0

        left , right = 0, len(height) - 1
        max_left,max_right = height[left], height[right]

        total_water = 0

        while left < right:

            if height[left] < height[right]:
                left += 1
                max_left = max(max_left, height[left])
                total_water += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                total_water += max_right - height[right]

        return total_water
