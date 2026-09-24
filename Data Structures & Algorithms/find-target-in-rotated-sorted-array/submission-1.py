class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid

            if nums[start] <= nums[mid]:
                # left is the sorted half
                if nums[start] <= target < nums[mid]:
                    # target is in left half
                    end = mid - 1
                else:
                    # target is in right half
                    start = mid + 1
            else:
                # right is the sorted half
                if nums[mid] < target <= nums[end]:
                    # target is in the right half
                    start = mid + 1
                else:
                    # target is possibly in the left half
                    end = mid - 1

        return -1