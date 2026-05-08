class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start, end = 0, len(nums)

        while start < end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid

        return -1