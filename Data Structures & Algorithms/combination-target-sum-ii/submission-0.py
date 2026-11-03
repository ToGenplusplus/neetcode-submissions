class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        res = []

        def backtrack(path, curr_sum, index):
            if curr_sum == target:
                res.append(list(path))
                return

            if curr_sum > target:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])
                backtrack(path, curr_sum + candidates[i], i + 1)
                path.pop()

        backtrack([], 0 , 0)
        return res

        """
            [3,1,2], target = 3 -> [[3], [1,2]]
            [],0,0
            
                [3],3,1
                    curr_sum = target -> return
                [1],1,2
                    curr_sum < target
                    [1,2],3,3
                    curr_sum == target -> return
                [2],2,3
                    curr_sum < target

        """