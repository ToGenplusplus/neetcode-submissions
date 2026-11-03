class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums)


        def backtrack(path: list[int]):
            if len(path) == len(nums):
                res.append(list(path))

            for i in range(len(nums)):
                # Skip if this element is already used in the current path
                if visited[i]:
                    continue

                # 1. Choose
                visited[i] = True
                path.append(nums[i])

                # explore deeper
                backtrack(path)

                #unchoose (backtrack)
                path.pop()
                visited[i] = False

        backtrack([])
        return res

