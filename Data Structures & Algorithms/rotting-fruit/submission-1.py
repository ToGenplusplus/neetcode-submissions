from collections import deque

class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return -1

        q = deque()

        m = len(grid)
        n = len(grid[0])
        fresh_count = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        time = 0
        directions = [(-1,0), (1,0), (0,1), (0, -1)]

        while q and fresh_count > 0:
            time += 1
            
            for _ in range(len(q)):
                rr,rc = q.popleft()
                print(f"{time}, row:{rr}, col:{rc}")

                for dr,dc in directions:
                    nr,nc = rr + dr, rc + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        q.append((nr,nc))

        return time if fresh_count == 0 else -1

        """
            if there are no rotten fruits - return -1
            bfs
                skip on
                    empty cell, already visited, rotten fruit, invalid (oob)

            Input: grid = 
            [
                [1,1,0],
                [0,1,1],
                [0,1,2]
            ]

            find first rotten fruit 
                g[2][2]
                    search neighbouring cells
                    [1][2]
                        - fresh, not visited, increase time += 1, mark visited
                            [0][2] - empty cell return
                            [2][2] - visited
                            [1][3] - invalid
                            [1][1] - 
                                - fresh, not visited, increase time += 1 (2), mark visited 
                                vist neighbours
                                [0][1]
                                    - fresh, not visited, increase time += 1 (3), mark visited 
                                    visit neighbours
                                    [-1][1] - invalid
                                    [1][1] - visited
                                    [0][0] - 
                                        - fresh, not visited, increase time += 1 (4), mark visited 
                                    [0][2] - empty
                                [2][1]
                                [1][0]
                                [1][2]
                    [3][2] - invalid 
                    [2][1] - 
                        - fresh, not visited, increase time += 1, mark visited
                        search neighbour cells
                            [1][1]
                            [3][1] - invalid
                            [2][0] - empty cell, return
                            [2][2] - already visited, return
                    [2][3] - invlaid


        [
            [1,0,1],
            [0,2,0],
            [1,0,1]
        ]

        """