class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        prevstep1 = 3
        prevstep2 = 2
        for step in range(4, n+1):

            current = prevstep1 + prevstep2

            prevstep2 = prevstep1
            prevstep1 = current

        return prevstep1
        
        """
        n = 1 , 0 steps
            n = 1
                o + 1
            n = 2
                0 +1 + 1
                0 + 2
                2 steps

            n = 3
            0 + 1 + 1 + 1
            0 + 1 + 2
            0 + 2 + 1
            3 steps

            n = 4
                since we can only take 1 or 2 steps
                4
                    -1 = 3 - we already know it takes 3 steps to get to step 3
                    -2 = 2 - we alredy know it takes 2 steps to get to step 2
                    total = 5 steps
            n = 5
                -1 = 4 - 5 steps
                -2 = 3 - 3 steps
                8 steps
            
        """