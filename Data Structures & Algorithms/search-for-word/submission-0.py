# my solution
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(row, col, index) -> bool:

            if index == len(word):
                return True

            if (row < 0 
                or row >= rows
                or col < 0
                or col >= cols
                or visited[row][col]
                or board[row][col] != word[index]):
                return False

            visited[row][col] = True

            found = (
                dfs(row + 1, col, index + 1)
                or dfs(row - 1, col, index + 1)
                or dfs(row, col + 1, index + 1)
                or dfs(row, col - 1, index + 1)
            )

            visited[row][col] = False

            return found


        for row in range(rows):
            for col in range(cols):
                if word[0] == board[row][col] and dfs(row, col, 0):
                    return True

        return False

        """
            have a dfs function that takes (row, col, index) as param and return bool

                check if index == len(word) - return True
                    ex; word = "CAT" index = 3

                return False for invalid states:
                    row < 0, row >= len(board)
                    col < 0, col >= len(board[0])
                    visited[row][col] is true
                    board[row][col] != word

                mark visited[row][col] = True
                check surrounding chars of board[row][col] by calling dfs on all 4 directions
            iterate through board until you find the
            firs char mathing word[0]
        """