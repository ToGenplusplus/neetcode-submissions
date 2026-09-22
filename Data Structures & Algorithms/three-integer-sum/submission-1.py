class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
            examples
                nums = [-1,0,1,2,-1,-4] -> [-1,-1,2],[-1,0,1]]

                nums = [0,1,1] -> []

                nums = [0,0,0] -> []

            constraints:
                len(nums) [3,3000]
                nums[i][-10^5, 10^5]
                does num contain duplicates
                is num sorted
                time complexity - O(n^2)
                space complexity - O(1)

            nums = [-1,0,1,2,-1,-4]
            nums_sorted = [-4,-1,-1,0,1,2]

            iterate throunh nums until i < len(nums) - 2
            *skip nums[i+1] if nums[i] == nums[i+1]
            if nums[i] >= 0, we can just skip (not going to find any j and k that can add to 0 )

            i | nums[i] ,j, nums[j], k, nums[k]
            1, -1,2,-1,5,2 -> sum 0 -> [[-1,-1,2]]
            2,-1,3,0,4,1 -> sum 0 -> [[-1,-1,2], [-1,0,-1]]
            3, 0, 4,1,5,2


            nums_sorted = [-4,-1,-1,0,1,2]

            i | nums[i] ,j, nums[j], k, nums[k]
            0, -4 , 1, 5,2 -> -3 < 0, k++
                k = 2, nums[k] == nums[k-1] skip nums[k]k++
                k = 3, -4 + 0 + 2= -2 k ++
                k = 4, -4 + 1 + 2 = -1 k++
                k =5 end inner loop i++
            1, -1, 2, -1, 5, 2 -> 0 -> [[-1,-1,2]]
                j = 3, k = 4 -1 + 0 + 2 = 1 > 0, k--
                k = 4, -1 + 0 + 1 = 0 -> [[-1,-1,2], [-1,0,1]]
            2, nums[i] == nums[i-1] skip
            3, 0, 4, 1, 5, 2 
                since nums[i] > 0 , break -> return result


                
            if looking for a bigger number k++
            else j--
            once we find i,j,k sum == 0
                move both j++ or k--
                if nums[j] != nums[j-1]
                j++
                nums[k] != nums[k+1]
                j--

        """

        if not nums:
            return []

        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break

            if i != 0 and nums[i] == nums[i - 1]:
                continue
            
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                        
                elif total > 0:
                    k -= 1
                else:
                    j += 1

        return result

                
