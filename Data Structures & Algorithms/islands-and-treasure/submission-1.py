from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        if not grid or not grid[0]:
            return 

        m = len(grid)
        n = len(grid[0])

        q = deque()
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    q.append((row, col))


        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:

            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] == -1:
                    continue

                if grid[nr][nc] > grid[r][c] + 1:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))



