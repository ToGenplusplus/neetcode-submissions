class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        if not m or not m[0]:
            return 

        n = len(m)
        for row in range(n - 1):
            for col in range(row + 1, n):
                m[row][col], m[col][row] = m[col][row], m[row][col]

        for row in range(n):
            m[row].reverse()
        """
            given 
                n x n matrix

            return
                None    
                    in place rotation of matrix 90 degrees clockwise

            examples
                 1 2 3
                 4 5 6
                 7 8 9

                 ->

                 7 4 1
                 8 5 2
                 9 6 3

            input -> transpose -> reverse rows

            1 2 3
            4 5 6 
            7 8 9

            1 4 7
            2 5 8
            3 6 9

            transpose logic
            n = 3, 
            r = 0
                col 1
                    swap m[0][2] with m[2][0]
                col 2
                    swap m[0][1] with m[1][0]
            r = 1
                col 2
                    swap m[1][2] with m[2][1]


            1 2 3 4
            5 6 7 8
            9 10 11 12
            13 14 15 16

            transpose

            1 5 9 13
            2 6 10 14
            3 7 11 15 
            4 8 12 16

            13 9 5 1
            14 10 6 2
            15 11 7 3
            16 12 8 4

            approach is to iterate through n x n starting from row 0 until n - 2
                start col is always row + 1

        """
