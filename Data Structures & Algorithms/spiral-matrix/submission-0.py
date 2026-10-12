class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
            given m(rows) x n(col) matrix
            1 2 3
            4 5 6
            7 8 9

            -> 
            all elements in spiral order
            [1,2,3,6,9,8,7,4,5]

            we need to track boundaries
            using this example
            1 2 3 4
            5 6 7 8
            9 10 11 12

            top starts at row 0
            right starts at col n - 1 = 3
            bottom starts at row m - 1 2
            left starts at col 0

            process top
                1 2 3 4
                top += 1 = 1
            process right
                8 , 12
                right -= 1 = 2
            process bottom
                11, 10 , 9
                bottom -= 1 = 1
                
            process left
                5
                left += 1 = 1
            ---
            top - 6, 7
            top += 1 = 2

             1 2 3 4
            5 6 7 8
            9 10 11 12
        """

        if not matrix or not matrix[0]:
            return []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        res = []

        while top <= bottom and left <= right:
            
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            if top <= bottom:

                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])

                bottom -= 1

            if left <= right:

                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res