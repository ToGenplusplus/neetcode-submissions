class Solution:
    def jump(self, nums: List[int]) -> int:
        """
            nums = [2,4,1,1,1,1]

            i, nums[i], jumps, current_end, farthest
            0, 2, 0,0 max(0,0 + 2) = 2
            1, 4, 1, 2, max(2, 1 + 4) = 5
            2, 1, 1, max(5, 2 + 1) = 5
            3, 1, 2, 5,
                current_end == len(nums) - 1, return jumps
        """

        jumps = current_end = farthest = 0

        for i in range(len(nums) - 1):
            if current_end >= len(nums) - 1:
                break

            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps