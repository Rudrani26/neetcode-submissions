class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.houserobber(nums[1:]), self.houserobber(nums[:-1]))
        #here the condition is first and last house both cant be picked together
        #so we solve house robber 1 2 times by skipping first and then the last house

    def houserobber(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            rob1, rob2 = rob2, max(rob1 + n, rob2)
        return rob2

        
        