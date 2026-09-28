class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """
            iterate throught nums 
                check if target - nums[i] in processed_nums
                    yes return index in processed nums and i
                put nums[i] = i in processed nums
        """

        if not nums:
            return []

        processed_nums = {}

        for i, num in enumerate(nums):
            if target - num in processed_nums:
                return [processed_nums[target - num], i]
            processed_nums[num] = i

        return []