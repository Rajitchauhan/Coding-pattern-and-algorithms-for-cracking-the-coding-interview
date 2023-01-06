"""


"""


class Solution:
    def solve(self , i , coins , amount):
        if i == 0:
            if (amount % coins[i]) == 0:
                return int(amount / coins[i])
            else:
                return 10000000
        no_take = 0 + self.solve(i-1 , coins , amount)
        take = float('inf')
        if coins[i] <= amount:
            take = 1 + self.solve(i , coins , amount - coins[i])
        return min(take , no_take)
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if len(coins) == 1:
            if amount % coins[0] == 0:
                return int(amount / coins[0])
            else:
                return -1

        return self.solve(len(coins)-1 , coins , amount)



""" memorization """
class Solution:
    def solve(self , i , coins , amount  , memo):
        if i == 0:
            if (amount % coins[i]) == 0:
                return int(amount / coins[i])
            else:
                return 10000000
        if memo[i][amount] != -1:
            return memo[i][amount]
        no_take = 0 + self.solve(i-1 , coins , amount , memo)
        take = float('inf')
        if coins[i] <= amount:
            take = 1 + self.solve(i , coins , amount - coins[i] , memo)
        memo[i][amount]  = min(take , no_take)
        return memo[i][amount]
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        memo = [[ -1 for j in range(amount+1)] for i in range(len(coins))]
        res = self.solve(len(coins)-1 , coins , amount , memo)
        if res == 10000000:
            return -1
        else:
            return res


""" Bottom up """
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [[0 for i in range(amount+1)] for j in range(len(coins))]
        for i in range(amount+1):
            if (i % coins[0]) == 0:
                dp[0][i] = i // coins[0]
            else:
                dp[0][i] = 10000000

        for i in range(1 , len(coins)):
            for j in range(amount+1):
                no_take = 0 +  dp[i-1][j]
                take = 10000000
                if coins[i] <= j:
                    take = 1 + dp[i][j - coins[i]]
                dp[i][j] = min(take , no_take)

        if dp[len(coins)-1][amount] == 10000000:
            return -1
        else:
            return dp[len(coins)-1][amount]
