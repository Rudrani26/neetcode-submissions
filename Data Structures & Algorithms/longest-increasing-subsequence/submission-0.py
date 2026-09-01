class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # LIS[i] represents the length of the longest increasing subsequence
        # starting at index i (including nums[i]).
        LIS = [1] * len(nums)  # Each number is at least an LIS of length 1.

        # Iterate backwards through the list
        # (We build from the end so that future values are already computed.)
        for i in range(len(nums) - 1, -1, -1):
            # Check all elements that come after nums[i]
            for j in range(i + 1, len(nums)):
                # If we can extend the increasing sequence
                if nums[i] < nums[j]:
                    # Update LIS[i] to the maximum length found so far
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        # The length of the overall longest increasing subsequence
        return max(LIS)
