class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        def find_area(row, col) -> int:
            if (
                row < 0 or row >= rows
                or col < 0 or col >= cols
                or grid[row][col] == 0
            ):
                return 0

            grid[row][col] = 0

            return 1 + (
                find_area(row + 1, col)
                +find_area(row - 1, col)
                +find_area(row, col + 1)
                +find_area(row, col - 1)
            )
            
        largest = 0
        for row in range(rows):
            for col in range( cols):
                if grid[row][col] == 1:
                    largest = max(largest, find_area(row, col))

        return largest