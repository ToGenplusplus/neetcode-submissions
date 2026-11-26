class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid or not grid[0]:
            return 0


        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col) -> int:
            if (
                row < 0 or row >= rows
                or col < 0 or col >= cols
                or grid[row][col] == 0
            ):
                return 0
            
            grid[row][col] = 0

            return 1 + (
                dfs(row + 1, col) + 
                dfs(row - 1, col) + 
                dfs(row, col + 1) + 
                dfs(row, col - 1)
            )

        max_area = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    island_area = dfs(row, col)
                    max_area = max(max_area, island_area)

        return max_area