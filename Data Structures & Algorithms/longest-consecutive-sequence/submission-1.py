class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0

        setNums = set(nums)

        for n in setNums:
            if (n-1) not in setNums:
                addLen = 1
                while (n + addLen) in setNums:
                    addLen += 1
                maxLength = max(addLen, maxLength)
        
        return maxLength