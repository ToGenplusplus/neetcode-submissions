class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
            given:
                int array

            result
                int - longest consecutive

            constraints
                nums sorted?
                nums contain duplicates
                expected time and space complexity? - O(n)
                len(nums)[]
                nums[i][]

            examples:
                nums = [2,20,4,10,3,4,5] -> 4
                2,3,4,5

                nums = [3] -> 1


                nums = [2,20,4,10,3,4,5]

                nums[i] is eiter beginning or part of a sequence - trying to determine which
                part of a sequence if nums[i] - 1 is in nums else beggining
                if nums[i] is start of a sequence
                    is nums[i] + 1 in nums - yes
                    is nums[i] + 2 in nums -  yes
                    etc..
                    keep checking for nums[i] + n in nums
                    keeping track of locallongest increase on each iteration
                    once we break out, we do a compare with the globa longest variable
                

                use a set to check for existence


                nums = [2,20,4,10,3,4,5]
                i | nums[i] | nums[i] - 1 in nums | is startOfSeq | maxLongest
                0 | 2 | 1 in nums is no | start of sequence | 1
                    3 in nums, yes , local_longest = 2
                    4 in nums, yes , local_longest = 3
                    5 in nums, yes , local_longest = 4
                    6 in nums, no, max_longes= max(m_l, lo_l) | 4

                1 | 20 | 19 not in nums | yes
                    21 not in nums, max_longes is still 4

                2 | 4 | 3 exists in nums, not start of seq, skip
                3 | 10, 9 not in nums, start of seq
                    11 not in nums, lol_long 1, max = 4
                4 | 3, 2 is in nums, skip
                5 | 4, 3 is in nums, skip
                6 | 5, 4 is in nums, skip

                end - max_longest - 4

                nums[1,0,-2,-1]

        """

        if not nums:
            return 0

        max_longest = 1

        nums_set = set(nums)

        for i in range(len(nums)):
            if nums[i] - 1 in nums_set:
                continue
            # beginning of a sequence
            local_longest = 1
            while nums[i] + local_longest in nums_set:
                local_longest += 1

            max_longest = max(max_longest, local_longest)

        return max_longest

        """
                nums[1,0,-2,-1]
        i | nums[i] | nums[i] - 1 in nums | is startOfSeq | maxLongest
        2 | -2 | -3 is not in nums, start of seq| 1
            -2 + 1  = -1 in nums, yes local_longest +=1 = 2
            -2 + 2  = 0 in nums, yes local_longest +=1 = 3
            -2 + 3  = 1 in nums, yes local_longest +=1 = 4
            -2 + 4  = 2 in nums, no, exit loop local_longest = 4 > 0 (max) max = 4

        3 | -1 | -2 is in nuns, not start of seq, so we skip
        end of processing nums
        - max_longest -> 4
        """

