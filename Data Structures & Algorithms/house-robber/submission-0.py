class Solution:
    def rob(self, nums: List[int]) -> int:
        #these two denote the house 1 behind and house 2 behind the current n
        rob1, rob2 = 0, 0

        for n in nums:
            rob1, rob2 = rob2, max(n + rob1, rob2)
        return rob2

        