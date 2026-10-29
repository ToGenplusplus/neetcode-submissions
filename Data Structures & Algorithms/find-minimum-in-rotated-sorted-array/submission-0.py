class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
            nums = [3,4,5,6,1,2], rotated 4 times
                note the index of the minimum notes how many times the array has been rotated

            so we know the minimum element in O(logn)

            scenario 1
            [3,4,5,6,1,2]
                mid is element 5, 
                    5 > 3 (left side is sorted)
                    5 > 2 (minimum is on right side)
            [6,1,2]
                mid is 1
                    1 < 2 (right side is sorted)
                    1 < 6 (left side must have minimum)
            [6,1]
                mid is 6
                    6 > 1 right side must have minimum
                [1]

            scenario 2

            [6,1,2,3,4,5]
                mid 2 < 5
                    search left
            [6,1,2]
                mid is 1
                search left
            [6,1]
                mid is 6
            search right
                [1] 
        """
        if nums[0] < nums[-1]:
            return nums[0]

        start, end = 0, len(nums) - 1

        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] <= nums[end]:
                end = mid
            else:
                start = mid + 1

        return nums[start]