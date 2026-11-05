class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        numIslands = 0

        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or grid[row][col] == "0"
            ):
                return

            grid[row][col] = "0"
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    numIslands += 1
                    dfs(row, col)

        return numIslands
        """
        0 0 1
        1 0 1
        0 1 0


        row , col, grid[row][col]
        0, 2, 1 
            mark 0
            call dfs on surrounding values
            1,2
                1, mark 0
                call dfs on surrounding values
                2,2 - 0
                0,2 - 0
                1,3 - invalid
                1,1 - 0
            0,1
            0,3 - invalid
            -1,2 - invalid
        """
        
        