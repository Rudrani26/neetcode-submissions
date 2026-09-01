class Solution:
    def climbStairs(self, n: int) -> int:
        one_step, two_step = 1, 1

        for i in range(n-1):
            one_step, two_step = two_step,  one_step + two_step
        
        return two_step       
        
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        
        # dp = [0] * (n+1)
        # dp[0] = 1
        # dp[1] = 1

        # for i in range(2, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[i]




        
# n = 5 : bottom up approach
# fibonacci series
# 8 5 3 2 1 1           
# 0 1 2 3 4 5