class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """ 
            n = [1,2,4,6]

            prefix product
            [1,1,2,8]

            suffix product
            [48,24,6,1]

            multiply result[i] = pp[i] * sp[i]

            to eliminate the extra space with the suffix product
            we can compute the suffx in constant

            suffix = 1
            result[n-1] = 1
            iterate through nums backwards
            i | nums[i] | pp[i] | suffix | res[i]
            3 | 6 | 8 | 1 | 8 * 1 = 8, suffix = suffix * nums[i] = 6
            2 | 4 | 8 | 1 | 8 * 1 = 8
        """

        if not nums:
            return []

        n = len(nums)
        results = [1] * n

        for i in range(1,n):
            results[i] = results[i-1] * nums[i - 1]

        suffix = 1

        for i in range(n - 1, -1, -1):
            results[i] *= suffix
            suffix *= nums[i]

        return results


        