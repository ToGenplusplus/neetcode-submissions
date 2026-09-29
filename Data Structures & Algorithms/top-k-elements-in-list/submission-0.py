from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
            nums = [2,1,3,2,3,4], k = 2

            n = len(nums) = 6 
            if nums does not have duplicates, and k <= # of unique elements
            in nums, there can be at most len(nums) unique elements

            there are 
            1 -> 1
            2 -> 2
            3 -> 2
            4 -> 1

            create a bucket of n+ 1
            [[],[1,4],[2,3],[],[],[],[]]

            index 1 has [1,4] -> frequency of 1,4 in nums is 1
            index 2 has [2,3] -> frequency of 2,3 in nums is 2

            iterate through the buckets lists from the end
            if bucket is not empty, append each element, once we reach
            k elements, return result

        """

        if not nums or k > len(nums):
            return []

        frequency = defaultdict(int)

        for num in nums:
            frequency[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in frequency.items():
            buckets[count].append(num)

        result = []

        for i in range(len(buckets) - 1, 0, -1):
            if buckets[i]:
                result.extend(buckets[i])

        return result[:k]