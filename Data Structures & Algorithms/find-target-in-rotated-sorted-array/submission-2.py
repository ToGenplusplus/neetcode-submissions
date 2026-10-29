class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start,end = 0, len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid

            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1

        """
            scenarios:
            nums = [3,4,5,6,1,2], target = 1
            start,end,mid,nums[mid],check,result
            0,5,2,5
                5 != target
                3 < 5, 1 not [3,5)
                start = mid + 1 = 3
            3,5,4
                nums[4] = 1 = target - return

            nums = [6,1,2,3,4,5], target = 1
            start,end,mid,nums[mid],check,result
            0,5,2,2
                2 != target
                2 > nums[start] but 1 not (2,5]
                end = mid -1 = 1
            0,1,0
                nums[0] = 6
                6 != target
                6 = nums start but 1 not (6,6)
                start = mid + 1 = 1
            1,1,1
                nums[mid] = 1 = target

            nums = [4,5,6,0,2,3], target = 1
            start,end,mid,nums[mid],check,result
            0,5,2,6
                6 != target
                6 > nums[start] but target not in [4,6)
                start = mid + 1 = 3
            3,5,4
                nums[4] = 2
                2 != target
                2 > 0(nums[start]) but 1 not in [0,2)
                start = mid + 1 = 5
            5,5,5
                nums[5] = 3 != target
                start = mid + 1 = 6
            6,5 - end of loop
        """