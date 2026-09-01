class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, a in enumerate(nums):
            #if a is greater than 0 then the total sum would never be 0 because the remaining 2 sumbers would only be larger than a
            if a > 0:
                break
            
            if i > 0 and a == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                threeSum = a + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([a, nums[left], nums[right]])
                    right -= 1
                    left += 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
            
        return result


        
        
        
        




        