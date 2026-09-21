class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """

            examples:
                nums = [1,2,4,6] -> [48, 24, 12, 8]

                nums = [-1,0,1,2,3] -> [0, -6, 0,0,0]

            constrainsts
                len(nums) []
                nums[i] []
                answer guaranteed to fit in an integer? 32bit
                expected time and space complexity?

            
            nums = [1,2,4,6] -> [48, 24, 12, 8]

            output = []
            calculate prefix product
            i | nums[i] | output[i - 1] * nums[i - 1] | output
            0 | 1 | 1 * 1 | [1]
            1 | 2 | 1 * 1 |[1, 1]
            2 | 4 | 1 * 2 | [1,1,2]
            3 | 6 | 2 * 4 | [1,1,2,8]

            [1,1,2,8] 
            calculating suffifx product
            i | nums[i] | suffix |  o[i] = output[i] * suffix | suffix = suffix * nums[i]
            3 | 6 | 1 | 8 * 1 | 8, suffix = suffix * nums[i] = 6
            2 | 4 | 6 | 2 * 6 = 12, s = 6 * 4 = 24
            1 | 2 | 24 | 1 * 24 = 24, s = 24 * 2 = 48
            0 | 1 | 48 | 1 * 48 = 48, s = 48 * 1 = 48

            return output[i]
        """

        if not nums:
            return []

        n = len(nums)
        output = [1] * n

        """
            nums = [-1,0,1,2,3]
            output = [1,1,1,1,1]
            calculate prefix product
            i | nums[i] |o[i] = output[i - 1] * nums[i - 1] | output
            1 | 0 | 1 * -1 = -1 | [1,-1,1,1,1]
            2 | 1 | 0 * -1 = 0 | [1,-1,0,1,1]
            3 | 2 | 0 * 1 = 0 | [1,-1,0,0,1]
            4 | 3 | 0 * 2 = 0 | [1,-1,0,0,0]
        """
        for i in range(1, n):
            output[i] = output[i - 1] * nums[i - 1]


        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        """
       Ouput = [1,-1,0,0,0]
       i | nums[i] | suffix |  o[i] = output[i] * suffix | suffix = suffix * nums[i]
       4 | 3 | 1 | 0 * 1 = 0 | 1 * 3 = 3
       3 | 2 | 3 | 0 * 3 = 0 | 3 * 2 = 6
       2 | 1 | 6 | 0 * 6 = 0 | 6 * 1 = 6
       1 | 0 | 6 | -1 * 6 = -6 | 6 * 0 = 0
       0 | -1 | 0 | 1 * 0 = 0 | 0
       end of loop -> return ouput = [0,-6,0,0,0]
        """

        return output

                