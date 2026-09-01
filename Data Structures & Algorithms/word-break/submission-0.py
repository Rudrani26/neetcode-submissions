class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Dynamic Programming array where dp[i] represents whether 
        # the substring s[i:] can be segmented into words from wordDict.
        dp = [False] * (len(s) + 1)

        # Base case: an empty string (after the last character)
        # can always be segmented (since there's nothing left to check).
        dp[len(s)] = True

        # Traverse the string from the end towards the beginning.
        for i in range(len(s) - 1, -1, -1):
            # Try every word in the dictionary.
            for w in wordDict:
                # Check if the substring starting at i is long enough 
                # to contain the current word 'w'.
                if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                    # If the word matches and the rest of the string 
                    # after it can be segmented, mark dp[i] as True.
                    dp[i] = dp[i + len(w)]

                    # Once dp[i] is True, we can stop checking further words.
                    if dp[i]:
                        break

        # dp[0] represents whether the entire string s can be segmented.
        return dp[0]
