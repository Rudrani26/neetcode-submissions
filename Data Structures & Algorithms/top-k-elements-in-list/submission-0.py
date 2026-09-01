class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #we count the frequency of each number

        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        #we create the freq butckets

        freq_bucket = [[] for i in range(len(nums) + 1)]

        #now we put the counted numbers in buckets
        for num, freq in count.items():
            freq_bucket[freq].append(num)

        results = []
        for i in range(len(freq_bucket) - 1, 0, -1):
            for num in freq_bucket[i]:
                results.append(num)
                if len(results) == k:
                    return results
        return results
        
        