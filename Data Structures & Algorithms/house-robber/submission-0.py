class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        maxes = [0] * n

        for i in range(n):

            if i == 0:
                maxes[i] = nums[0]
            elif i == 1:
                maxes[i] = nums[0] if nums[0] > nums[i] else nums[i]
            else:
                maxes[i] = max(maxes[i - 1], maxes[i - 2] + nums[i])

        return maxes[n - 1]

        """
            nums = [2,9,8,3,6]
            i | nums[i] | maxes[i]
            0 | 2 | 2
            1 | 9 | 9
            2 | 8 | max(9, 8 + 2) = 10
            3 | 3 | max(10, 9 + 3) = 12
            4 | 6 | max(12, 10 + 6) = 16

        """
        """
            nums = [2,9,8,3,6] -> 16

            [2] - 2
            [2,9] 
                choices
                    2 or 9
            [2,9,8] - max is 10
                choices
                    2,
                    9,
                    8
                    2 and 8 - max
            [2,9,8,3]
                choices
                    2,9,8,3
                    2 and 8 - 10
                    2 and 3 - 5
                    9 and 3 - 12 - max is 12
            [2,9,8,3,6]
                choices
                    2,9,8,3,6
                    2 + 8 + 6 = 16
                    2 + 3 = 5
                    2 + 6 = 8
                    9 + 3 = 12
                    9 + 6 = 15
                    8 + 6 = 14

        """