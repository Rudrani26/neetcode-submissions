class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        bucket = defaultdict(list)

        for n, freq in count.items():
            bucket[freq].append(n)
        
        result = []

        for freq in range(len(nums), 0, -1):
            for n in bucket[freq]:
                result.append(n)

                if len(result) == k:
                    return result
        