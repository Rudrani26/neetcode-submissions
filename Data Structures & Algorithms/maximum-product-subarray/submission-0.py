class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #set current max and current min to 1 as the base
        curr_max, curr_min = 1, 1
        #setting result to the first number in the list
        res = nums[0]

        #looping through each number to store the max min product
        for n in nums:
            temp = curr_max * n
            curr_max = max(n, curr_max*n, curr_min*n)
            curr_min = min(n, temp, curr_min*n)
            res = max(res, curr_max)
        
        return res

        