class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
            nums = [1,2,0,1,0] -> true
                0, 1, index 0 + 1 = 1
                1,2 
                    index 1 + 2 3

            nums = [1,2,1,1,1] -> true
            nums = [1,2,2,0,1] -> true
            nums = [1,1,0,2,1] -> false
            nums = [1,2,1,0,1] -> false

        """
        n = len(nums)
        goal = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False