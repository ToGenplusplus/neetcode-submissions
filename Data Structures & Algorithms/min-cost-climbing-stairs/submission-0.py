class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        prev2 = cost[0]
        prev1 = cost[1]
        total = 0

        for step in range(2, len(cost)):
            current = cost[step] + min(prev2, prev1)

            prev2 = prev1
            prev1 = current

        return min(prev1, prev2)
