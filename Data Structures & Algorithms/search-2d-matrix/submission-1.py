class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        if target > matrix[m-1][n-1] or target < matrix[0][0]:
            return False


        start = 0 
        end = (m * n) - 1

        while start <= end:
            mid = start + (end - start) // 2
            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                start = mid + 1
            else:
                end = mid - 1


        return False
        """
            matrix m x n 
                m rows
                n columns
                sorted non decreasing order
                first integer of ever row is greater that the last integer of the previous row

            target integer

            output
                true -> target is in matrixs
                fals -> target is not in matrix

            examples
                matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10 -> true

                matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15 -> false

            constraints
                m,n [1,100]
                matrix[i][j], target [-10000,10000]
                time - O(log(m * n))
                space - O(1)

            matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

                m = 3
                n = 4 
                total of 12 ints

                how do i get row 1, col 2
                5 % 3 = 2
                5 // 3 = 1

                5 // 4 = 1
                5 % 4 = 1

                row 

                start | end | start + (end - start) // 2 | row = mid // n | col = mid % n | matrix[row][col]
                0, 11, 5, 1, 1, 11 > 10 end = mid - 1 = 4
                0, 4, 2, 0, 2, 4 < 10, start = mid + 1
                3 , 4, 3, 0, 3, 8 < 10, start - mid + 1
                4, 4, 4, 10, = target -> true 
                -- target is now 15
                0, 11, 5, 1, 1, 11 < 15 start = mid + 1 = 6
                6, 11, 8, 2, 0, 14 < 15 start = mid + 1 = 9
                9, 11, 10, 2, 2, 30 > 15 end = mid - 1 = 9
                9,9, 9, 20 > 15, end = mid - 1 = 8
                end < start - end loop, target not found return false
        """