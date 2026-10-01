from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if not nums or target == None:
            return []

        processed_nums = defaultdict(int)

        for i, num in enumerate(nums):
            required = target - num
            if required in processed_nums:
                return [processed_nums[required],i]
            processed_nums[num] = i

        return []