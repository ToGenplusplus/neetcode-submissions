class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        def dfs(curr_path, index) -> None:
            
            res.append(curr_path.copy())

            for i in range(index, len(nums)):
                curr_path.append(nums[i])
                dfs(curr_path, i + 1)
                curr_path.pop()

        dfs([], 0)
        return res