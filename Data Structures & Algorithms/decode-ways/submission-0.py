class Solution:
    def numDecodings(self, s: str) -> int:
        #base case that there is one way to decode i.e the whole number
        dp = {len(s) : 1}

        #start from the end
        for i in range(len(s) - 1, -1, -1):
        #edge cases if 0 then 0 ways, otherwise 1 number has 1 way
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            
        #two digit decode
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                dp[i] += dp[i+2]
        
        return dp[0]

# "226"
# 226 -> 3:1
# i = 2, "22 6"
# not 0 so 2:1
# i = 1, "2 26"
# not 0 so 1: 1
# i+1 = 2, less than len(s) = 3
# so dp[1] = dp[1] + dp [2] = 2
# hence 1: 2
# i = 0
# not 0 so 0: 1
# i+1 = 1, less than len(s) = 3
# so dp[0] = dp[0] + dp [1] = 1 + 2 = 3
# hence 0: 3
# Final answer dp[0] = 3
        
        