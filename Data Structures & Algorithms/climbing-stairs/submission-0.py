class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 3:
            return n

        values = [None] * (n + 1)
        for i in range(4):
            values[i] = i

        def find_ways (number: int):
            print(f"{number}")
            if values[number - 1] == None:
                values[number - 1] == find_ways(number - 1)
            if values[number - 2] == None:
                values[number - 2] == find_ways(number - 2)

            values[number] = values[number - 1] + values[number - 2]
            return values[number]

        return find_ways(n)

        
        """
            target = n = 5

            n = 0 -> 0
            n = 1
                0 + 1 ->  1
            n = 2
                0 + 1 + 1 = 2
                0 + 2 = 2
                -> 2 ways
            n = 3
                can either take 1 or 2 steps to get to 3
                step 2 (take 1 step)
                    i know there are 2 ways to get to step 2
                step 1 (take 2 steps)
                    i know there is 1 way to get to step 1
                total 3 ways to get to step 3

                0 + 1 + 1 + 1
                0 + 1 + 2
                0 + 2 + 1

            n = 4
                can either take 1 or 2 steps to get to 4
                step 3 (take 1 step)
                    3 ways to get to step 3
                step 2 (take 2 steps)
                    2 ways to get to step 2
                total 5 ways to get to step 4

                
                0 + 1 + 1 + 1 + 1
                0 + 1 + 1 + 2
                0 + 1 + 2 + 1
                0 + 2 + 1 + 1
                0 + 2 + 2


        """