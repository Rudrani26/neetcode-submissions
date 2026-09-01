class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #we use hashset to have lookup of all distinct numbers
        numSet = set(nums)
        longest_seq = 0

        for num in numSet:
            if num - 1 not in numSet:
                num_count = 1
                while num + num_count in numSet: #if num=1, num_count =1, check if 1+1=2 is in set
                    num_count += 1
                longest_seq = max(num_count, longest_seq)
        
        return longest_seq



        