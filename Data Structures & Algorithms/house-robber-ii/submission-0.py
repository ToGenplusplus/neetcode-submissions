class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses: list[int]) -> int:
            prev_2 = 0
            prev_1 = houses[0]

            for i in range(1, len(houses)):
                curr = max(houses[i] + prev_2, prev_1)

                prev_2 = prev_1
                prev_1 = curr
            
            return max(prev_1, prev_2)

        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))

        """
            nums = [2,9,8,3,6]

            n = len(nums)
            if n == 1, return nums[0]
            [2]
            if n == 2, return 0
            [2,9] -max = 0
            n == 3
            [2,9,8]
                n = 3
                i = n- 1 = 2

                cannot touch house[0] r house[2], max is house[1] = 9

        """
