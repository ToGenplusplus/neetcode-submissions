class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:


        min_at_i = [amount + 1] * (amount + 1)
        min_at_i[0] = 0

        for curr_amt in range(1, amount + 1):

            for coin in coins:
                if curr_amt - coin >= 0:
                    min_at_i[curr_amt] = min(min_at_i[curr_amt], 1 + min_at_i[curr_amt - coin])

        return min_at_i[amount] if min_at_i[amount] != amount + 1 else -1

       
        """
            coins = [1,5,10], amount = 12
            12
                11
                    10 6 1

                7
                2
                    1
                        0 - min is 3

            
            coins = [1,2,3,5], amount = 8

            8
                7
                6
                5
                3
                    2
                    1
                    0 - min 2

            c(0) = 0
            c(1) = 1 + min(c(0)) = 1
            c(2) = 
                1 + min(c(1), c(0)) = 1
            c(3) =
                1 + min(c(2), c(1), c(0)) = 1
            c(4) = 
                1 + min(c(3), c(2), c(1)) = 2
        """