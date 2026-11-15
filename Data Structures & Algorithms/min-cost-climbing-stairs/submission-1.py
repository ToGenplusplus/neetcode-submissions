class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2, len(cost)):
            c_cost = cost[i] + min(prev1, prev2)

            prev2 = prev1
            prev1 = c_cost

        return min(prev1, prev2)
        """
            cost = [1,2,1,2,1,1,1]

            step
            7
                6, cost[6] = 1 
                    5, cost[5] = 1
                        4, cost[4] = 1
                            3, cost[3] = 2
                                2, cost[2] = 1
                                    1, cost[1] = 2
                                    0, cost[0] = 1
                                1, cost[1] = 2
                            2, cost[2] = 1
                                1, cost[1] = 2
                                0, cost[0] = 1
                        3, cost[3] = 2

                    4, cost[4] = 1

                5, cost[5] = 1
                    4, cost[4] = 1
                    

                    3, cost[3] = 2


        cost = [1,2,1,2]
        top = 4
            4
                3, c= 2
                    2, c= 1 (2)
                        1, c= 2 - total = 5
                        0, c= 1 - total 4
                    1, c= 2 - total = 4
                2, c= 1
                    1, c=2 - total = 3
                    0, c= 1 - total = 2 - min

        """