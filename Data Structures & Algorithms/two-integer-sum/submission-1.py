class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # we maintain a dictionary which stores the visited number as the key and its index as the value
        prevVisited = {}

        #we iterate through the array to calculate the difference between the current number and the target and difference is what we check if it present in the previously visited dictionary, if yes we return those indices
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevVisited:
                return [prevVisited[diff],i]
            prevVisited[n] = i

        