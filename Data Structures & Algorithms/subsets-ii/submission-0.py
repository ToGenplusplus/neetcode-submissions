class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        def backtrack(path, index):

            res.append(list(path))

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i -1]:
                    continue

                path.append(nums[i])
                backtrack(path, i + 1)
                path.pop()


        backtrack([], 0)
        return res
        """
            [1,2,1] -> [[],[1],[1,2],[1,1],[1,2,1],[2]]

            sort [1,1,2]

            [],0
                add [] to res -> [[]]

                [1],1
                    add [1] to res -> [[], [1]]
                        [1,1],2
                        add [1,1] to res -> [[], [1], [1,1]]
                            [1,1,2],3
                                add [1,1,2] to res -> [[], [1], [1,1], [1,1,2]]
                        [1,2],3
                         add [1,2] to res -> [[], [1], [1,1], [1,1,2]]

                skip index 1 (duplicate)
                [2],3
                    add [2] to res -> [[], [1], [1,1], [1,1,2],]

            iterate through index to len(nums)
                skip duplicate elements
        """

        