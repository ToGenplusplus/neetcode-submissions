from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return

        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647

        q = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row,col))

        directions = [(-1,0), (1,0), (0,1), (0, -1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF):
                    grid[nr][nc] = min(grid[nr][nc], grid[r][c] + 1)
                    q.append((nr,nc))
        
        """ 
            Input: [
                [0,  -1, 2147483647],
                [2147483647,2147483647, 0],
                [-1, 2147483647, -1]
            ]

            chests = [(0,0), (1,2)]

            (0,0)
                bfs, valid cells: (1,0), mark 1
                    bfs (1,0), valid cells: (1,1), mark 2
                        bfs(1,1), valid cells: (2,1) - mark 3
                            bfs(2,1), no valid cells
            state after:
            [
                [0,-1, INF],
                [1,2,0],
                [-1,3,-1]
            ]

            bfs (1,2), valid: (0,2), (1,1)
                level 1
                bfs(0,2), mark 1, valid: none
                bfs (1,1) 1 < 2, mark 1, valid: (2,1), (1,0)
                    level 2
                    bfs (2,1), 2 < 3, mark 2, valid: none
                    bfs (1,0), 2 > 1, leave 1, valid: none
            state after
            [
                [0,-1, 1],
                [1,1,0],
                [-1,2,-1]
            ]


            Input: [
                [2147483647,-1,0,2147483647],
                [2147483647,2147483647,2147483647,-1],
                [2147483647,-1,2147483647,-1],
                [0,-1,2147483647,2147483647]
            ]

            2 treasure chest locations ((0,2), (3,0))
            valid cells: not out of bounds, not (0 or -1)
            bfs on (0,2)
                valid: (1,2), (0,3) - level 1 (mark with 1)
                bfs on (1,2)
                    valid (2,2), (1,1) - level 2 (mark with 2)
                    bfs on (2,2)
                        valid (3,2) - level 3
                        bfs on (3,2)
                            valid (3,3) - level 4
                            bfs(3,3) - no valid, return

        """

