class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        n = len(nums)

        res = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                return res

            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif total < 0:
                    j+=1
                else:
                    k -= 1
        return res
        """

            nums = [-1,0,1,2,-1,-4]

            sort nums
            [-4,-1,-1,0,1,2]
            n = 6
            i,j,k
            0,1,5
                nums[0] + nums[1] + nums[5] = -3 < 0
                j+=1=2
                nums[0] + nums[2] + nums[5] = -3 < 0
                j+=1=3
                nums[0] + nums[3] + nums[5] = -2 < 0
                j+=1 = 4
                nums[0] + nums[4] + nums[5] = -1 < 0
                j+=1 = 5
                j = k, exist
            1,2,5
                nums[1] + nums[2] + nums[5] = 0 -> [-1,-1,2] to result
                j is < k, j+=1=3, k-=1 = 4
                nums[1] + nums[3] + nums[3] = 0 -> [-1,0,1] to result
                j is < k, j+=1=4, k-=1 = 3
                k > j - exit

            2,3,5
                nums[i] = nums[i -1] skip
            3,4,5
                nums[3] + nums[4] + nums[5] = 3 > 0, k-=1 = 4
                k = j, exit

            since next i = n-2, we exit and return result

            O(n log n) - sort , O(n^2), n = 3000 = (3 * 10^3)^2 = 10 ^ 6
        """