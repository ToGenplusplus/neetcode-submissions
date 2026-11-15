class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        house_2 = 0
        house_1 = nums[0]

        for i in range(1,len(nums)):
            c_choice = max(house_1, nums[i] + house_2)

            house_2 = house_1
            house_1 = c_choice

        return max(house_1, house_2)
        """
            nums = [1,1,3,3]

            i = 1
                rob house 1 - 1
                skip it because i already robbed house 0 - 1

            i = 2
                rob house 2, 3 + house[0](1) = 4 - max
                skip - i chose to rob house 1 = 1

            i = 3
                rob house 3, 3 + house[1](1) = 4 
                skip, robbed house[2] = 4
                max is 4
            

        """