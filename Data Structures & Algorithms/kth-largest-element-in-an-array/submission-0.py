from heapq import heapify, heappush, heappushpop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapify(heap)

        for num in nums:

            if len(heap) < k:
                heappush(heap, num)
            elif num > heap[0]:
                heappushpop(heap, num)

        return heap[0] if heap else 0
        """
            let n = len(nums)
            nums = [2,3,1,5,4], k = 2

            sort nums (O n log n)
            [1,2,3,4,5]

            return nums[n - k]

            without sorting, we can use a heap of size k

            nums = [2,3,1,1,5,5,4], k = 3

            i | nums[i] | operation | result
            0, 2, heap is empty, insert -2 into heap
            1, 3, -nums[i] is < heap[0] - add to heap, heap= [-3, -2]
            2, 1, -nums[i] is > heap[0], skip
            3, 1, -nums[i] is > heap[0], skip
            4, 5, -nums[i] is < heap[0], add to heap, heap= [-5, -3, -2]
            5, 5, -nums[i] is <= heap[0], len(heap) == k so we replace
        """