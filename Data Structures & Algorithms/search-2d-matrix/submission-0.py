class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # validate input
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        start, end = 0, m * n

        while start < end:
            mid = start + (end - start ) // 2

            row = mid // n
            col = mid % n

            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                start = mid + 1
            else:
                end = mid

        return False

