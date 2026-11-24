class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
            if len(nums) == 1, return nums[0]

            nums = [2,-3,4,-2,2,1,-1,4]

            max = curr = nums[0]

            iterate through nums starting from index 1

            i, nums[i], curr_sum, max_sum
            1, -3, max(-3, 2 + -3) -1, 2
            2, 4, max(4, 4 + -1)4, 4
            3, -2, max(-2, -2 + 4),2,4
            4, 2, max(2, 2 + 2)4, 4
            5, 1, max(1, 4 + 1)5, 5
            6, -1, max(-1, 5 + -1),4, 5
            7, 4, max(4, 4 + 4)8, 8

            return 8
        """
        if not nums:
            return 0

        max_sum = curr_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum
        