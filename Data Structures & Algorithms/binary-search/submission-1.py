class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        """
            nums = [-1,0,2,4,6,8], target = 4
            s,e,mid, nums[mid]
            0,5,mid,2, < target search right (start = mid + 1)
            3,5,4,6 > target search left (end = mid - 1)
            3,3,3,4 = target -> return 3

            nums = [-1,0,2,4,6,8], target = 3
            s,e,mid, nums[mid]
            0,5,2,2, < target search right (start = mid + 1)
            3,5,4,6 > target search left(end = mid - 1)
            3,3,3,4 > target search left(end - mid - 1)
            3,2 - end is less than 2, exit search and return -1
        """

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return -1 