class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        """
            given
                nums 
                    integer array
                    len(nums) range [2, 10^5]
                    nums[i] range [-30, 30]
                    each produt is guaranteed to fit in a 32-it integer

            return
                output - integer array 
                    

            constraints
                time complexity - O(n) , no division operator


            examples 
                nums = [4,2,1,6] -> [12, 24, 48, 8]

                prefix product of nums:
                [1, 4, 8, 8] 

                suffix product of nums:
                [12, 6, 6, 1]


                p[i] * s[i] = o[i]
                i | p[i] |s[i] | res
                0 | 1, 12, 12
                1, 4, 6, 24
                2, 8, 6, 48
                3 8, 1, 8
                -> [12, 24,48, 8]

                instead of a suffix product array
                we can compute the suffix on the fly and update 
                the prefix product[i] with the results

                output = prefix product
                initate s = 1
                we iterate through nums backwrds 
                    o [i] = p[i] * s
                    s = s * nums[i]
        """

        if not nums:
            return []

        n = len(nums)
        output = [1] * n

        for i in range(1, n):
            output[i] = nums[i - 1] * output[i - 1]

        s = 1

        for i in range(n - 1 , -1, -1):
            output[i] *= s
            s *= nums[i]

        return output


