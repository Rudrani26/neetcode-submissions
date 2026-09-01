class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize a DP array where dp[a] represents the minimum number of coins 
        # needed to make up the amount 'a'. 
        # Start by setting all values to amount + 1 (a large number that acts as "infinity")
        dp = [amount + 1] * (amount + 1)
        
        # Base case: 0 coins are needed to make the amount 0
        dp[0] = 0

        # Iterate over all amounts from 1 to the target amount
        for a in range(1, amount + 1):
            # For each coin, try to make up the amount 'a'
            for c in coins:
                # Only consider the coin if it doesn't exceed the current amount
                if a - c >= 0:
                    # Choose the minimum between:
                    #   - the current dp[a] value (previous best)
                    #   - using the current coin (1 coin + best solution for remaining amount a - c)
                    dp[a] = min(dp[a], 1 + dp[a - c])

        # If dp[amount] is still the initialized large number, it means it's not possible
        # to form the target amount with the given coins.
        return dp[amount] if dp[amount] != amount + 1 else -1
