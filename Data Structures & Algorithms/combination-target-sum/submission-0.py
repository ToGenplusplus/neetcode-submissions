class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:

        result = []

        def backtrack(path, curr_sum, index):
            if curr_sum == target:
                result.append(list(path))
                return
            elif curr_sum > target:
                return
            else:

                for i in range(index, len(nums)):
                    path.append(nums[i])
                    backtrack(path, curr_sum + nums[i], i)
                    path.pop()

        backtrack([], 0, 0)
        return result
        """
        nums = [2,4,6] t = 6 -> [[2,2,2], [2,4], [6]]

        [], 0, 0
            0
                [2],2,0
                    [2,2],4,0
                        [2,2,2],6,0
                        [2,2],4,1
                    [2],2,1
                [],0,1
                    [4],4,1
                        [4,4],8,1 - return
                    [],0,2
                        [6],6,2 - target - return
            1

            2

            i = 0, curr_sum = 0, include num[i](2)
                curr_sum += num[i] = 2
                2 < target

                call again with curr_sum(2), i = 0

                    curr_sum += num[i] = 4
                    4 < target
                    call again with curr_sum(4), i = 0
                        curr_sum += num[i] = 6
                        6 = target, add to result, return

                call with curr_sum(2), i = 1

                [2,2]
                    [2,2,2]
                        sum = target
                        add to result
                        return
                [2,4]
                    sum = target, add to result return 
                    

            [4]

                [4,4]
                    sum = 8 > target, return

            [6]
                sum = target, add to result, return
        """

